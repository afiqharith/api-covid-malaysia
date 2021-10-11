from assets import MOH_RESTAPI as RESTAPI

app = RESTAPI().run_app

if __name__ == "__main__":
    app.run(debug = True)
