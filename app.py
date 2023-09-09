from flask import Flask,render_template
import pickle

popular_df = pickle.load(open('E:\SAMPLE_PRoJECTS\product_recommendation\popularity_df.pkl','rb'))
# pt = pickle.load(open('pt.pkl','rb'))
# books = pickle.load(open('books.pkl','rb'))
# similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           product_name = list(popular_df['sub_category'].values),
                           image=list(popular_df['image'].values),
                           votes=list(popular_df['ratings'].values),
                           price=list(popular_df['actual_price'].values)
                           )


if __name__ == '__main__':
    app.run(debug=True)    