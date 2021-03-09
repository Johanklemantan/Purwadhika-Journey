from flask import Flask, render_template, request
import plotly
import plotly.graph_objs as go
import pandas as pd
import json
app = Flask(__name__)
tips = pd.read_csv('./static/tips.csv')
def category_plot(
    cat_plot = 'histplot',
    cat_x = 'sex', cat_y = 'total_bill',
    estimator = 'count', hue = 'smoker'):
    if cat_plot == 'histplot':
        data = []
        for val in tips[hue].unique():
            hist = go.Histogram(
                x=tips[tips[hue]==val][cat_x],
                y=tips[tips[hue]==val][cat_y],
                histfunc=estimator,
                name=val
            )
            data.append(hist)
        
        title = 'Histogram'
    elif cat_plot == 'boxplot':
        data = []
        
        for val in tips[hue].unique():
            box = go.Box(
                x=tips[tips[hue]==val][cat_x],
                y=tips[tips[hue]==val][cat_y],
                name=val
            )
            data.append(box)      
        title = 'Box'
    if cat_plot == 'histplot':
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title='person'),
            boxmode='group'
        )
    else:
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title='person'),
            boxmode='group'
        )
    result = {'data': data, 'layout': layout}

    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
    
@app.route('/')
def home():
    plot = category_plot()
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('sex', 'Sex'), ('smoker', 'Smoker'), ('day', 'Day'), ('time', 'Time')]
    list_y = [('total_bill', 'Bill'), ('tip', 'Tip'), ('size', 'Size')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('sex', 'Sex'), ('smoker', 'Smoker'), ('day', 'Day'), ('time', 'Time')]

    return render_template(
        'category.html',
        plot=plot,
        focus_plot='histplot',
        focus_x = 'sex',
        focus_estimator='count',
        focus_hue='smoker',
        drop_plot=list_plot,
        drop_x=list_x,
        drop_y=list_y,
        drop_estimator=list_est,
        drop_hue=list_hue
    )

@app.route('/cat_fn/<nav>')
def cat_fn(nav):
    
    if nav == True:
        cat_plot = 'histplot'
        cat_x = 'sex'
        cat_y = 'total_bill'
        estimator = 'count'
        hue = 'smoker'

    else:
        cat_plot = request.args.get('cat_plot')
        cat_x = request.args.get('cat_x')
        cat_y = request.args.get('cat_y')
        estimator = request.args.get('estimator')
        hue = request.args.get('hue')
    if estimator == None:
        estimator = 'count'
    if cat_y == None:
        cat_y = 'total_bill'

    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('sex', 'Sex'), ('smoker', 'Smoker'), ('day', 'Day'), ('time', 'Time')]
    list_y = [('total_bill', 'Bill'), ('tip', 'Tip'), ('size', 'Size')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('sex', 'Sex'), ('smoker', 'Smoker'), ('day', 'Day'), ('time', 'Time')]

    plot = category_plot(cat_plot, cat_x, cat_y, estimator, hue)
    return render_template(
        'category.html',
        plot=plot,
        focus_plot=cat_plot,
        focus_x = cat_x,
        focu_y = cat_y,
        focus_estimator=estimator,
        focus_hue=hue,
        drop_plot=list_plot,
        drop_x=list_x,
        drop_y=list_y,
        drop_estimator=list_est,
        drop_hue=list_hue
    )

@app.route('/scatt_fn')
def scatt_fn():
    pass

@app.route('/pie_fn')
def pie_fn():
    pass

@app.route('/db_fn')
def db_fn():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)