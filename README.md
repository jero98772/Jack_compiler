# Jack Compiler 

A web-based Jack language compiler that converts Jack code to VM code using FastAPI backend and a modern web interface.

## 🚀 Features

- **Web-based Interface**: Modern, responsive UI for writing and compiling Jack code
- **Real-time Compilation**: Instant feedback with syntax highlighting
- **Example Library**: Pre-loaded Jack code examples to get started quickly
- **Error Handling**: Detailed error messages and compilation feedback
- **REST API**: Clean API endpoints for programmatic access


## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jero98772/Jack_compiler
   cd Jack_compiler
   ```

2. **Install dependencies**:
   ```bash
   pip install -r 
   ```
## 🚀 Running the Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```


The application will be available at:
- **Web Interface**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Alternative API Docs**: http://localhost:8000/redoc


## 🎯 Usage Examples

### Web Interface
1. Open http://localhost:8000 in your browser
2. Select an example from the grid or write your own Jack code
3. Click "Compile" to generate VM code
4. View the output in the right panel


