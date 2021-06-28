from nia import create_app

app = create_app()


if __name__=='__main__':
    app.run(debug=True, host="192.68.1.104", port = 8090)
    #app.run(debug=True, port = 5000)
