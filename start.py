import multiprocessing
import os
from app import app # Flask/FastAPI app

def run_bot():
    os.system("python main.py")

if __name__ == "__main__":
    # Jalankan bot di proses terpisah
    p = multiprocessing.Process(target=run_bot)
    p.start()
    
    # Jalankan web server
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
