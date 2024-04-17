from flask import Flask, request
from flask_apscheduler import APScheduler
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)
scheduler = APScheduler()

# @scheduler.task('interval', id='my_job', seconds=10)
# def my_job():
#     print('This job is executed every 10 seconds.')

@app.route('/api/v1/scrape', methods=['POST'])
def scrape_news():
    data = request.get_json()
    type = data["type"]
    print(type)
    return { "success": True }, 200

if __name__ == '__main__':
    scheduler.init_app(app)
    # scheduler.start()
    app.run(debug=True, port=5000)