from assets import MOH_WebAPI as WebAPI
import datetime

app = WebAPI().run_app

if __name__ == "__main__":
    try:
        app.run(debug = True)
    except KeyboardInterrupt:
        print(f"Server shutting down on {datetime.datetime.now}")
