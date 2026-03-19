# Vercel wrapper for Streamlit
def handler(request):
    import subprocess
    import os
    
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Run streamlit
    result = subprocess.run(
        ["streamlit", "run", "app_new.py", "--server.port=8501"],
        capture_output=True,
        text=True
    )
    
    return {"statusCode": 200, "body": "Streamlit started"}
