
# Data Source

We collected recipes from [Tasty website](https://tasty.co/). The elements we scraped include recipe title, description, ingredients, and preparation steps. We collected around 2000 recipes. However, due to limited budget, we were only able to annotate 800 of them. Our annotations are divided into five categories: Appetizer/side-dish, Main course, Dessert, Drinks, and others. To explore more, please feel free to play around with our page by searching ingredients or food related key words and filter your search result using the drop down menu. Curious how we used our annotated data for predicting food category? please check out our Machine Learning page. 


# Project Introduction


We collected recipes from [Tasty website](https://tasty.co/). The elements we scraped include recipe title, description, ingredients, and preparation steps. We collected around 2000 recipes. However, due to limited budget, we were only able to annotate 800 of them. Our annotations are divided into five categories: Appetizer/side-dish, Main course, Dessert, Drinks, and Other.

We used Amazon Mechanical Turk annotate the recipes  based on tge categeries and for each recipe, we assign it to three different workers. Then, we extracted the best annotation if two annotators agree on one category. We investigated the inter-annotator agreement and we chose to use Krippendorff’s phi and alpha here because we have five categories(Appetizers/Side dish, Main course, Dessert, Drinks and Other). Based on Krippendorff’s alpha result, the observed disagreement is high (57.375%). The alpha is around 0.42, below the lowest conceivable limit (0.667), and falls into the range of (0.41, 0.6) as being moderate.

Instructions for files:
1. `frontend.html`, `frontend.css`, `frontend.js` are three frontend files contain the interface design and the logic for interactions.
2. In the folder [InformationRetrival](https://github.ubc.ca/piggyeq/COLX_523_Project/tree/master/milestone4/InformationRetrival), we have `search.py` file which is the main algorithm for our searching functionality.
3. In the folder [MachineLearning](https://github.ubc.ca/piggyeq/COLX_523_Project/tree/master/milestone4/MachineLearning/linearSVC), we have the main algorithm for LinearSVC implemented Python file.
4. `Visualizations.py` is the file that generates the visualization charts. Details are demonstrated in the `Visualizations and stats.ipynb` file.
5. `backend.py` the main python code for hosting a backend server.
6. `frontend_documentation.md` is the text file that introduces the functionalities for the web.

