# app.py
from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

# 学生数据
students_data = [
    {"id": "S1", "name": "电热壶", "resume": "<h2>电热壶</h2><p><strong>姓名：</strong>电热壶</p><p><strong>职业：</strong>烧水专家</p><p><strong>个人简介：</strong>我能在3分钟内将常温水加热至沸腾，具备自动断电、防干烧等高级技能。是现代家庭不可或缺的饮水解决方案提供者。</p><p><strong>技能：</strong>快速加热、保温、自动断电。</p>"},
    {"id": "S2", "name": "叙利亚", "resume": "<h2>叙利亚</h2><p><strong>全名：</strong>叙利亚阿拉伯共和国</p><p><strong>定位：</strong>文明古国，亚洲西部国家</p><p><strong>个人简介：</strong>拥有数千年历史的文明摇篮，首都大马士革被誉为'天国里的城市'。我见证了帝国的兴衰更迭，承载着深厚的历史与文化底蕴。</p><p><strong>地标：</strong>帕尔米拉古城、倭马亚清真寺。</p>"},
    {"id": "S3", "name": "吴彦祖", "resume": "<h2>吴彦祖</h2><p><strong>姓名：</strong>吴彦祖 (Daniel Wu)</p><p><strong>职业：</strong>演员、导演、制片人</p><p><strong>个人简介：</strong>出生于美国加州，毕业于俄勒冈大学建筑系。1997年前往香港开始演艺生涯，凭借出众的外貌和扎实的演技迅速走红，成为华语影坛的标志性人物之一。</p><p><strong>代表作：</strong>《新警察故事》、《美少年之恋》、《窃听风云》系列。</p>"},
    {"id": "S4", "name": "奢室", "resume": "<h2>奢室</h2><p><strong>名称：</strong>奢室 (SHE'S)</p><p><strong>定位：</strong>轻奢生活方式品牌</p><p><strong>个人简介：</strong>致力于为追求品质生活的现代都市人群提供兼具设计感与实用性的家居好物。从香薰、摆件到收纳，每一件产品都诠释着对'轻奢'的理解，让生活充满仪式感。</p><p><strong>理念：</strong>'奢'不在价高，而在精致；'室'不仅是空间，更是心境。</p>"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def get_students():
    return jsonify(students_data)

@app.route('/student/<student_id>')
def get_student_resume(student_id):
    student = next((s for s in students_data if s['id'] == student_id), None)
    if student:
        return jsonify({"resume": student['resume']})
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
