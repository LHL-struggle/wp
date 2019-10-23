import requests
from flask import Flask, render_template, request, make_response, jsonify
app = Flask(__name__)

def movie_ranking(type_id):
    rsp = {}
    url = "https://movie.douban.com/j/chart/top_list?type=%s&interval_id=100:90&action=&start=0&limit=20" % type_id
    type_name_data = requests.get(url).json()
    rsp["movie_data"] = type_name_data
    print(rsp)
    return rsp

@app.route("/")
def home():
    return render_template("index.html")

def refer():
    headers = request.headers  # 返回字典
    # print(headers)
    # 获取Referer值
    referer = headers.get("Referer")
    # print(referer)
    if referer is None:  # 如果是爬虫则不存在referer
        return 1
    return 0

@app.route("/zj")
def zj():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("传记.html")

@app.route("/er")
def er():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("儿童.html")

@app.route("/mx")
def mx():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("冒险.html")

@app.route("/jq")
def jq():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("剧情.html")

@app.route("/dz")
def dz():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("动作.html")

@app.route("/dh")
def dh():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("动画.html")

@app.route("/ls")
def ls():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("历史.html")

@app.route("/gz")
def gz():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("古装.html")

@app.route("/tx")
def tx():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("同性.html")

@app.route("/xj")
def xj():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("喜剧.html")

@app.route("/qh")
def qh():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("奇幻.html")

@app.route("/jt")
def jt():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("家庭.html")

@app.route("/kb")
def kb():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("恐怖.html")


@app.route("/xy")
def xy():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("悬疑.html")

@app.route("/js")
def js():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("惊悚.html")

@app.route("/zz")
def zz():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("战争.html")

@app.route("/gw")
def gw():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("歌舞.html")


@app.route("/wx")
def wx():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("武侠.html")

@app.route("/zn")
def zn():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("灾难.html")

@app.route("/aq")
def aq():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("爱情.html")

@app.route("/fz")
def fz():
    return render_template("犯罪.html")

@app.route("/dp")
def dp():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("短片.html")

@app.route("/kh")
def kh():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("科幻.html")

@app.route("/jlp")
def jlp():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("纪录片.html")

@app.route("/xb")
def xb():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("西部.html")

@app.route("/yd")
def yd():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("运动.html")

@app.route("/yy")
def yy():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("音乐.html")

@app.route("/hs")
def hs():
    if refer():
        return "想爬吗，你爬不到"
    return render_template("黑色电影.html")

@app.route("/movie_rank")
def movie_rank():
    type_id = request.args.get("type_id")
    rsp = movie_ranking(type_id)
    # print(rsp)
    resp = make_response(rsp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with, content-type'
    return resp

if __name__ == "__main__":
    # debug=True 表示测试模式
    app.run(host="192.168.9.162", port=80, debug=True)