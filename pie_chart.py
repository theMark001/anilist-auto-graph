#                                               ​                      ⣇⣿⠘⣿⣿⣿⡿⡿⣟⣟⢟⢟⢝⠵⡝⣿⡿⢂⣼⣿⣷⣌⠩⡫⡻⣝⠹⢿⣿⣷                                                    #
#                                               ​                      ⡆⣿⣆⠱⣝⡵⣝⢅⠙⣿⢕⢕⢕⢕⢝⣥⢒⠅⣿⣿⣿⡿⣳⣌⠪⡪⣡⢑⢝⣇                                                    #
#                                               ​                      ⡆⣿⣿⣦⠹⣳⣳⣕⢅⠈⢗⢕⢕⢕⢕⢕⢈⢆⠟⠋⠉⠁⠉⠉⠁⠈⠼⢐⢕⢽                                                    #
#                                               ​                      ⡗⢰⣶⣶⣦⣝⢝⢕⢕⠅⡆⢕⢕⢕⢕⢕⣴⠏⣠⡶⠛⡉⡉⡛⢶⣦⡀⠐⣕⢕                                                    #
#                                               ​                      ⡝⡄⢻⢟⣿⣿⣷⣕⣕⣅⣿⣔⣕⣵⣵⣿⣿⢠⣿⢠⣮⡈⣌⠨⠅⠹⣷⡀⢱⢕                                                    #
#                                               ​                      ⡝⡵⠟⠈⢀⣀⣀⡀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢈⡋⠴⢿⡟⣡⡇⣿⡇⡀⢕                                                    #
#                                               ​                      ⡝⠁⣠⣾⠟⡉⡉⡉⠻⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣦⣥⣿⡇⡿⣰⢗⢄                                                    #
#                                               ​                      ⠁⢰⣿⡏⣴⣌⠈⣌⠡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣉⣉⣁⣄⢖⢕⢕⢕                                                    #
#                                               ​                      ⡀⢻⣿⡇⢙⠁⠴⢿⡟⣡⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣵⣿                                                    #
#                                               ​                      ⡻⣄⣻⣿⣌⠘⢿⣷⣥⣿⠇⣿⣿⣿⣿⣿⣿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                                    #
#                                               ​                      ⣷⢄⠻⣿⣟⠿⠦⠍⠉⣡⣾⣿⣿⣿⣿⣿⣿⢸⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟                                                    #
#                                               ​                      ⡕⡑⣑⣈⣻⢗⢟⢞⢝⣻⣿⣿⣿⣿⣿⣿⣿⠸⣿⠿⠃⣿⣿⣿⣿⣿⣿⡿⠁⣠                                                    #
#                                               ​                      ⡝⡵⡈⢟⢕⢕⢕⢕⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⠿⠋⣀⣈⠙                                                    #
#                                               ​                      ⡝⡵⡕⡀⠑⠳⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⡠⡲⡫⡪⡪⡣                                                    #

import matplotlib.pyplot as plt

# Function for plotting pie charts
def plot_pie_chart(my_dict, title):
    
    # Create two lists to store the keys and values of the dictionary, and assign them to variables
    data_labels = list(my_dict.keys())
    data_amount = list(my_dict.values())

    # Create variables to store the colors of the pie chart slices and set the necessary offsets between slices
    colors = ['#664753', '#656432', '#33576E', '#385E63', '#655633', '#4C4766', '#404465']
    explode = [0.05] * len(data_amount)
    
    # The function creates a figure and axes within it, returning two objects: fig (Figure) and ax (Axes)
    fig, ax = plt.subplots()

    # Set the background color
    fig.patch.set_facecolor('#323D44')
    
    # The function creates the pie chart, which accepts the configuration arguments (wedges - segments, texts - labels, autotexts - percentages). Also, specify the arguments such as data, colors, explode, percent format, and text color
    wedges, texts, autotexts = ax.pie(data_amount,
                                      colors=colors,
                                      explode=explode,
                                      autopct='%1.0f%%',
                                      textprops={'color': "#B4BDB7"})
    
    # Then, create a loop where the edge color of the slice is changed depending on the slice's color
    for wedge, color in zip(wedges, colors):
        if color == '#664753':
            wedge.set_edgecolor('#FF6384')
            continue
        elif color == '#33576E':
            wedge.set_edgecolor('#37A2EB')
            continue
        elif color == '#656432':
            wedge.set_edgecolor('#FFD700')
            continue
        elif color == '#385E63':
            wedge.set_edgecolor('#4BC0C0')
            continue
        elif color == '#655633':
            wedge.set_edgecolor('#FFA500')
            continue
        elif color == '#4C4766':
            wedge.set_edgecolor('#9966CC')
            continue
        elif color == '#404465':
            wedge.set_edgecolor('#6A5ACD')
    
    # Create the pie chart legend, set the position, disable the background color of the legend, set the text color of the legend, disable borders, and so on
    ax.legend(wedges, data_labels, loc='center left', bbox_to_anchor=(0.85, 0, 0.5, 1), facecolor='none', edgecolor='none', labelcolor='#B4BDB7')

    # Set the title color
    ax.set_title(title, color='#B4BDB7')

    # Ensure the pie chart is circular
    ax.axis('equal')

    # Parameter to allow multiple windows without stopping the code
    plt.show(block=False)