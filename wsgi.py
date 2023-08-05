from assets import WebAPI
import datetime
import os

app = WebAPI().run_app

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    except KeyboardInterrupt:
        print(f"Server shutting down on {datetime.datetime.now}")
