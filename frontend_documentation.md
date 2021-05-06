# Documentation of our frontend files

Our frontend has three main parts: html files, css file and javascript file.

## HTML Files

The HTML files provides the frontend interface layout. We have two HTML files. The first html file, `frontend.html` is to construct the main page. The main page has data visualization, project introduction, search and filter features, and a machine learning button that will lead to another html page `machine.html`. When people click the data visualization, it will show a pop-up page consists of corpus statistics and word cloud based on our annotated data. When people click the project introduction button, it will show a pop-up page showing explanation of our project. 

The search bar is used to search key words of recipes and can be filtered by the categories in the dropdown menus. The submit button has `onclick="update_page()"` method and it will send a request to backend. 

For the `machine.html` page, we have a `home` button that leads us back to the main page. In addition to that, the input box is used to insert the input of our machine learning model. The submit button has `onclick="machine_page()"` method that will send a request to backend to run the prediction using our model. 

## CSS

The `frontend.css` provides a cascading style sheet file that we used to format the design of the webpage. It allows us to customized design properties of our webpage. Some of the main elements of the css file includes `.button-container{}`, `.imgContainer{}`, `.maintext{}`, `popup1{}`, and `.recipe-input{}`. 

* The `.button-container{}` customizes the design for data visualization, project introduction, and machine learning buttons. 

* The `.imgContainer{}` aligns the images on the center of both html pages.

* The `.maintext{}` customizes the padding, alignment, color, and font-size of the main text.

* The `popup1{}` customizes the padding, box size, alignment, text style, color, and font-size of the pop-up pages for the data visualization and project introduction. 

* The `.recipe-input{}` designs margin, height, and padding of the input box for `machine.html` page.

To summarize, the cascading style sheet defines design properties for the html file.


## Javascript

The frontend.js has two main functions: `update_page()` and `machine_page()`.

* The `update_page()` will update the response and return recipes on the same page based on the input in the search form of `frontend.html`.

* The `machine_page()` will update the output of the predictions on the same page based on the input on the `machine.html`.
