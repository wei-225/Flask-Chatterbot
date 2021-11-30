from app import app
import logging

if __name__ == "__main__":
    # print out url map
    app.logger.setLevel(logging.INFO)
    app.logger.info(app.url_map)
    app.run(host="127.0.0.1", debug=True, use_reloader=False)
