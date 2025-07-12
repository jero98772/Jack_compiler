from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
import os
import sys

# Import the Jack compiler
from tools.jackcompiler import JackTokenizer, CompilationEngine

app = FastAPI(title="Jack Compiler API", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Sample Jack code examples
EXAMPLES = {
    "simple_arithmetic": {
        "name": "Simple Arithmetic",
        "code": """class Main {
    function void main() {
        do Output.printInt((3 * 2) + 1);
        return;
    }
}"""
    },
    "square_class": {
        "name": "Square Class",
        "code": """class Square {
    field int x, y;
    field int size;
    
    constructor Square new(int Ax, int Ay, int Asize) {
        let x = Ax;
        let y = Ay;
        let size = Asize;
        do draw();
        return this;
    }
    
    method void draw() {
        do Screen.setColor(true);
        do Screen.drawRectangle(x, y, x + size, y + size);
        return;
    }
    
    method void moveUp() {
        if (y > 0) {
            do Screen.setColor(false);
            do Screen.drawRectangle(x, (y + size) - 1, x + size, y + size);
            let y = y - 2;
            do Screen.setColor(true);
            do Screen.drawRectangle(x, y, x + size, y + 1);
        }
        return;
    }
}"""
    },
    "control_structures": {
        "name": "Control Structures",
        "code": """class Main {
    function void main() {
        var int i;
        let i = 0;
        while (i < 10) {
            if (i > 5) {
                do Output.printInt(i);
            }
            let i = i + 1;
        }
        return;
    }
}"""
    },
    "array_example": {
        "name": "Array Example",
        "code": """class ArrayTest {
    function void main() {
        var Array arr;
        var int i;
        
        let arr = Array.new(5);
        let i = 0;
        
        while (i < 5) {
            let arr[i] = i * 2;
            let i = i + 1;
        }
        
        let i = 0;
        while (i < 5) {
            do Output.printInt(arr[i]);
            let i = i + 1;
        }
        
        do arr.dispose();
        return;
    }
}"""
    },
    "string_example": {
        "name": "String Example",
        "code": """class StringTest {
    function void main() {
        var String message;
        let message = "Hello, World!";
        do Output.printString(message);
        do Output.println();
        return;
    }
}"""
    }
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/examples")
async def get_examples():
    """Get all available examples"""
    return EXAMPLES

@app.post("/api/compile")
async def compile_jack(request: Request):
    data = await request.json()
    jack_code = data.get("jack_code", "")

    tokenizer = JackTokenizer(jack_code)
    engine = CompilationEngine(tokenizer)
    engine.compile_class()
    
    vm_code = engine.get_vm_code()
    
    return JSONResponse(content={
        "vm_code": vm_code,
        "success": True,
        "error": ""
    })



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
