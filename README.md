# CRUD_Python_MONGO

## MOTIVATION
The motivation behind this project is to create a CRUD Python module that serves the purpose of performing CRUD operations on a MongoDB. The project's primary goal is to develop an interactive dashboard using Dash, a Python web application framework. The dashboard connects to a MongoDB database through an AnimalShelter class and loads the data into a Pandas Data Frame. The dashboard's layout includes a title with a logo and a unique identifier, interactive filtering options for selecting rescue types, a data table for displaying animal data with sorting and pagination, a pie chart showing breed percentages based on the chosen filter, and a geo-location chart pinpointing the location of selected animals. Users can select from three rescue types or choose the "Reset" option to reset the dashboard to its initial state. Additionally, the dashboard offers interactive features like clicking on data table rows to view animal locations and clicking on the logo to open a specified URL. The project focuses on data visualization and customization, while some warning messages related to Plotly Express and Pandas are present but do not impact the dashboard's functionality.

The project leverages a combination of powerful tools to deliver its essential functionality. MongoDB serves as the model component, offering a flexible and scalable NoSQL database solution that accommodates semi-structured animal shelter data. The integration with Python through PyMongo for data retrieval and manipulation. Dash, a web framework developed by Plotly, forms the backbone of the web application, enabling the creation of interactive data visualization dashboards. It utilizes Python libraries like Pandas, Plotly Express, and Dash-Leaflet to craft dynamic interfaces. Pandas plays a pivotal role in data manipulation and transformation, while Plotly Express simplifies the generation of engaging charts and graphs. Dash-Leaflet enhances the application with interactive maps. JupyterDash facilitates the development and testing of Dash applications within the Jupyter environment. Base64 encoding is employed to embed images, such as logos, directly into the HTML structure. These tool choices were made for their compatibility, versatility, and capacity to streamline the development process, resulting in a robust and user-friendly animal shelter dashboard.

The completion of the animal shelter dashboard project involved several essential steps and the effective utilization of various technologies. Initially, data was extracted from a MongoDB database using PyMongo, and the retrieved data was structured into a Pandas DataFrame. The Dash framework played a pivotal role in designing the dashboard's layout, which included a title, logo, interactive filtering options, a data table, and visualizations such as a pie chart and geographic map. Interactive filtering allowed users to select specific rescue types, dynamically updating the displayed data. Challenges during development, such as the display of the pie chart and map side by side and refining the "Reset" filter functionality, were overcome through iterative development and collaboration. The final deployment enabled access to the dashboard via a local server, providing an intuitive and informative tool for analyzing animal shelter data.

## INSTALLATION

Python: Python is a versatile programming language suitable for a variety of applications, including data manipulation, web services, and integration with databases. The script provided is written in Python.
To install you can download Python from https://www.python.org/downloads/

animal_shelter Module: This custom module contains the AnimalShelter class, which provides CRUD operations for managing animal records. As the script is built around this module, it's essential for its functionality.

MongoDB:  MongoDB is a popular NoSQL database that allows for flexible schema and JSON-like document storage. The AnimalShelter class interacts with MongoDB to manage animal records. Follow this document for installation https://www.mongodb.com/docs/manual/installation/

Dash: Dash is a Python framework for building interactive web applications. It enables the creation of web-based data visualization dashboards with ease. You can install Dash using pip with the command pip install dash.

Dash-Leaflet: Dash-Leaflet is an extension of Dash that provides interactive maps for web applications. You can install it using pip with the command pip install dash-leaflet.

Plotly Express: Plotly Express is a Python library for creating interactive visualizations. It simplifies the process of generating charts and graphs. You can install Plotly Express using pip with the command pip install plotly.

JupyterDash: JupyterDash is a library that allows you to develop and test Dash applications within the Jupyter Notebook environment. You can install it using pip with the command pip install jupyter-dash.

Base64: Base64 encoding is used to embed images directly into the HTML structure. Python includes a base64 module that can be used for encoding and decoding data in base64. No additional installation is required.

## CODE EXAMPLE

Insert:
  


Read

 
 

Update
 

 

Delete
 
 







Reset Filter
 ![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/852023d4-16c2-4efe-bc5d-0d5da1cc0a10)





