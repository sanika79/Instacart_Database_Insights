def meanOrderFrequency(path_to_dataset):
    """
    Displays the mean order frequency by utilizing the orders table.
    :param path_to_dataset: this path should have all the .csv files for the dataset
    :type path_to_dataset: str
    """
    assert isinstance(path_to_dataset, str)
    import pandas as pd
    order_file_path = path_to_dataset + '/orders.csv'
    orders = pd.read_csv(order_file_path)
    print('On an average, people order once every ', orders['days_since_prior_order'].mean(), 'days')
    
    
def numOrdersVsDays(path_to_dataset):
    """
    Displays the number of orders and how this number varies with change in days since last order.
    :param path_to_dataset: this path should have all the .csv files for the dataset
    :type path_to_dataset: str
    """
    
    assert isinstance(path_to_dataset, str)
    
    import pandas as pd 
    import numpy as np 
    import matplotlib.pyplot as plt 
    import matplotlib
    
    
    
    order_file_path = path_to_dataset + '/orders.csv'
    
    orders = pd.read_csv(order_file_path)
    
    order_by_date = orders.groupby(by='days_since_prior_order').count()
    
    fig = plt.figure(figsize = [15, 7.5])
    ax = fig.add_subplot()
    order_by_date['order_id'].plot.bar(color = '0.75')
    ax.set_xticklabels(ax.get_xticklabels(), fontsize= 15)
    plt.yticks(fontsize=16)
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x))))
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x/1000))))
    ax.set_xlabel('Days since previous order', fontsize=16)
    ax.set_ylabel('Number of orders / 1000', fontsize=16)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_children()[7].set_color('0.1')
    ax.get_children()[14].set_color('0.1')
    ax.get_children()[21].set_color('0.1')
    ax.get_children()[30].set_color('0.1')
    my_yticks = ax.get_yticks()
    plt.yticks([my_yticks[-2]], visible=True)
    plt.xticks(rotation = 'horizontal');
    
    

def numOrderDaysSizeBubble(path_to_dataset):
    """
    Plots a bubble plot in which:
    x: Days since Previous Order
    y: Number of orders/1000
    size: Average Size of order given it was placed on x
    
    :param path_to_dataset: this path should have all the .csv files for the dataset
    :type path_to_dataset: str
    """
    import numpy as np
    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    assert isinstance(path_to_dataset, str)
    
    
    order_file_path = path_to_dataset + '/orders.csv'
    order_product_prior_file_path = path_to_dataset + '/order_products__prior.csv'
    
    orders = pd.read_csv(order_file_path)
    order_products_prior = pd.read_csv(order_product_prior_file_path)
    
    order_id_count_products = order_products_prior.groupby(by='order_id').count()
    orders_with_count = order_id_count_products.merge(orders, on='order_id')
    order_by_date = orders.groupby(by='days_since_prior_order').count()
    # take above table and group by days_since_prior_order

    df_mean_order_size = orders_with_count.groupby(by='days_since_prior_order').mean()['product_id']
    df_mean_order_renamed = df_mean_order_size.rename('average_order_size')


    bubble_plot_dataframe = pd.concat([order_by_date['order_id'], df_mean_order_renamed], axis=1)

    bubble_plot_dataframe['average_order_size'].index.to_numpy()

    fig = plt.figure(figsize=[15,7.5])
    ax = fig.add_subplot()
    plt.scatter(bubble_plot_dataframe['average_order_size'].index.to_numpy(), bubble_plot_dataframe['order_id'].values, s=((bubble_plot_dataframe['average_order_size'].values/bubble_plot_dataframe['average_order_size'].values.mean())*10)**3.1, alpha=0.5, c = '0.5')

    plt.xticks(np.arange(0, 31, 1.0));
    ax.xaxis.grid(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('Days since previous order', fontsize=16)
    ax.set_ylabel('Number of orders / 1000', fontsize=16)
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x))))
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x/1000))))
    my_yticks = ax.get_yticks()
    plt.yticks([my_yticks[-2], my_yticks[0]], visible=True);

    fig = plt.figure(figsize=[10,9])
    ax = fig.add_subplot()
    plt.scatter(bubble_plot_dataframe['average_order_size'].index.to_numpy()[:8], bubble_plot_dataframe['order_id'].values[:8], s=((bubble_plot_dataframe['average_order_size'].values[:8]/bubble_plot_dataframe['average_order_size'].values.mean())*10)**3.1, alpha=0.5, c = '0.5')

    plt.xticks(np.arange(0, 8, 1.0));
    ax.xaxis.grid(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('Days since previous order', fontsize=16)
    ax.set_ylabel('Number of orders / 1000', fontsize=16)
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x))))
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x/1000))))
    my_yticks = ax.get_yticks()
    plt.yticks([my_yticks[-2], my_yticks[0]], visible=True);
    
    
def orderTimeHeatMaps(path_to_dataset):
    """
    Plots the distribution of order with respect to hour of day and day of the week.
    :param path_to_dataset: this path should have all the .csv files for the dataset
    :type path_to_dataset: str
    """
    
    assert isinstance(path_to_dataset, str)
    
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    
    order_file_path = path_to_dataset + '/orders.csv'
    
    orders = pd.read_csv(order_file_path)

    grouped_data = orders.groupby(["order_dow", "order_hour_of_day"])["order_number"].aggregate("count").reset_index()
    grouped_data = grouped_data.pivot('order_dow', 'order_hour_of_day', 'order_number')

    grouped_data.index = pd.CategoricalIndex(grouped_data.index, categories=[0,1,2,3,4,5,6])
    grouped_data.sort_index(level=0, inplace=True)

    plt.figure(figsize=(12,6))
    hour_of_day = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14','15','16', '17', '18', '19','20', '21', '22', '23']
    dow = [ 'SUN', 'MON', 'TUES', 'WED', 'THUR','FRI','SAT']  

    ax = sns.heatmap(grouped_data, xticklabels=hour_of_day,yticklabels=dow,cbar_kws={'label': 'Number Of Orders Made/1000'})
    cbar = ax.collections[0].colorbar
    cbar.set_ticks([0, 10000, 20000, 30000, 40000, 50000])
    cbar.set_ticklabels(['0','10.0','20.0','30.0','40.0','50.0'])
    ax.figure.axes[-1].yaxis.label.set_size(15)
    ax.figure.axes[0].yaxis.label.set_size(15)
    ax.figure.axes[0].xaxis.label.set_size(15)

    ax.set(xlabel='Hour of Day', ylabel= "Day of the Week")
    ax.set_title("Number of orders made by Day of the Week vs Hour of Day", fontsize=15)
    plt.show()

    grouped_data = orders.groupby(["order_dow", "order_hour_of_day"])["order_number"].aggregate("count").reset_index()
    grouped_data = grouped_data.pivot('order_dow', 'order_hour_of_day', 'order_number')

    grouped_data.index = pd.CategoricalIndex(grouped_data.index, categories=[0,1,2,3,4,5,6])
    grouped_data.sort_index(level=0, inplace=True)

    plt.figure(figsize=(12,6))
    hour_of_day = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14','15','16', '17', '18', '19','20', '21', '22', '23']
    dow = [ 'SUN', 'MON', 'TUES', 'WED', 'THUR','FRI','SAT']  

    ax = sns.heatmap(np.log(grouped_data), xticklabels=hour_of_day,yticklabels=dow,cbar=False)
    cbar = ax.collections[0].colorbar

    ax.figure.axes[-1].yaxis.label.set_size(15)
    ax.figure.axes[0].yaxis.label.set_size(15)
    ax.figure.axes[0].xaxis.label.set_size(15)


    ax.set(xlabel='Hour of Day', ylabel= "Day of the Week")
    ax.set_title("Number of orders made by Day of the Week vs Hour of Day (Log Scale)", fontsize=15)
    plt.show()
    
def generateWordCloud(path_to_dataset):
    """
    Generates word cloud.
    :param path_to_dataset: path to dataset
    :type path_to_dataset: str
    """
    
    assert isinstance(path_to_dataset, str)
    
    from wordcloud import WordCloud
    import pandas as pd
    import matplotlib.pyplot as plt
    
    product_path = path_to_dataset + "/products.csv"
    aisles_path = path_to_dataset + "/aisles.csv"
    departments_path = path_to_dataset + "/departments.csv"
    order_product_prior_path = path_to_dataset + "/order_products__prior.csv"

    df_products = pd.read_csv(product_path)
    df_aisles = pd.read_csv(aisles_path)
    df_departments = pd.read_csv(departments_path)
    df_order_products_prior = pd.read_csv(order_product_prior_path)

    # Merge Prior orders, Product, Aisle and Department 
    df_order_products_prior_merged = pd.merge(
                                        pd.merge(pd.merge(df_order_products_prior, df_products, on="product_id", how="left"), 
                                            df_aisles, 
                                            on="aisle_id", 
                                            how="left"), 
                                        df_departments, 
                                        on="department_id", 
                                        how="left")
    # Top N products by frequency
    top_products = df_order_products_prior_merged["product_name"].value_counts()


    d = top_products.to_dict()

    wordcloud = WordCloud(background_color='white')
    wordcloud.generate_from_frequencies(frequencies=d)
    plt.figure(figsize = (8,8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def no_of_orders(path_to_data = './instacart-market-basket-analysis'):
    """
    pass path to orders.csv
    """
    
    bins = 10
    path = path_to_data + '/orders.csv'
    import numpy as np # linear algebra
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd 
    import numpy as np 
    import matplotlib.pyplot as plt 
    import matplotlib.mlab as mlab
    import seaborn as sns 
    from scipy.optimize import curve_fit
    from IPython.display import display, HTML
    
    
    orders = pd.read_csv(path) 
    sns.set_style('dark')
    customer_no = orders.groupby("user_id", as_index = False)["order_number"].max() 
    
    n, bins, patches = plt.hist(customer_no["order_number"] , bins, color='blue', alpha=0.5)

    plt.xlabel("No. of Orders")
    plt.ylabel("Count")
    plt.title("Number of Orders per Customer")


def freq_product(path1 = "./instacart-market-basket-analysis/order_products__train.csv",path2 = "./instacart-market-basket-analysis/order_products__prior.csv" , path3 = "./instacart-market-basket-analysis/products.csv"):
    import numpy as np # linear algebra
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd 
    import numpy as np 
    import matplotlib.pyplot as plt 
    import matplotlib.mlab as mlab
    import seaborn as sns 
    from scipy.optimize import curve_fit
    from IPython.display import display, HTML
    order_products_train = pd.read_csv(path1) 
    order_products_prior = pd.read_csv(path2)
    products = pd.read_csv(path3)
    t_p = order_products_train.append(order_products_prior,ignore_index = True)
    prod = t_p.groupby("product_id",as_index = False)["order_id"].count() 

    top = 20
    product_Count = prod.sort_values("order_id",ascending = False)
    df1 = product_Count.iloc[0:top,:]
    df1 = df1.merge(products,on = "product_id")
    display(df1.loc[:,["product_name"]])
    
def dept_prod(m = "./instacart-market-basket-analysis/products.csv" , n = "./instacart-market-basket-analysis/departments.csv" , p = "./instacart-market-basket-analysis/aisles.csv"):
    import numpy as np # linear algebra
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd 
    import numpy as np 
    import matplotlib.pyplot as plt 
    import matplotlib.mlab as mlab
    import seaborn as sns 
    from scipy.optimize import curve_fit
    from IPython.display import display, HTML
    products = pd.read_csv(m)
    departments = pd.read_csv(n) 
    aisles = pd.read_csv(p)
    x = pd.merge(left=products, right=departments, how='left')
    lists = pd.merge(left = x, right=aisles, how='left')
    
    group_list = lists.groupby("department")["product_id"].aggregate({'Total_products': 'count'}) 
    final = group_list.reset_index() 
    final.sort_values(by='Total_products', ascending=False, inplace=True)
    
    sns.set_style('white') 
    ax = sns.barplot(x="Total_products", y="department", data=final,color = 'gray' )

    r = ax.spines["right"].set_visible(False)
    t = ax.spines["top"].set_visible(False)


def dept_reorder(path = "order_products__prior.csv" , m = "products.csv" , n = "departments.csv" , p = "aisles.csv"):
    import numpy as np # linear algebra
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd 
    import numpy as np 
    import matplotlib.pyplot as plt 
    import matplotlib.mlab as mlab
    import seaborn as sns 
    from scipy.optimize import curve_fit
    from IPython.display import display, HTML
    products = pd.read_csv(m)
    departments = pd.read_csv(n) 
    aisles = pd.read_csv(p)
    
    order_products_prior = pd.read_csv(path)
    
    order_products_prior = pd.merge(order_products_prior, products, on='product_id', how='left')
    order_products_prior = pd.merge(order_products_prior, aisles, on='aisle_id', how='left')
    order_products_prior = pd.merge(order_products_prior, departments, on='department_id', how='left')
    
    df2 = order_products_prior.groupby(["department"])["reordered"].aggregate("mean").reset_index()

    plt.figure(figsize=(12,8))
    sns.set_style('white')

    ax1 = sns.scatterplot(df2['reordered'].values,df2['department'].values , color = 'gray')
    plt.ylabel('Department', fontsize=15)
    plt.xlabel('Reorder Ratio' , fontsize=15)
    plt.title("Department wise reorder ratio", fontsize=15)
    plt.xticks(rotation='horizontal')
    r = ax1.spines["right"].set_visible(False)
    t = ax1.spines["top"].set_visible(False)
    plt.show() 