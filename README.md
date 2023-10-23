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

To use the module, you first need to import the ‘AnimalShelter’ class from your module into your Python script or application. You can do this using the ‘import’ statement:
from animal_shelter import AnimalShelter

Now create an initialization of the AnimalShelter class, you can achieve this by calling its constructor and providing the required credentials for connection to your MongoDB database. 
shelter = AnimialShelter()

You can now use the ‘shelter’ object to perform CRUD operations on the MongoDB database. 

Create (Insert): To insert a new document or record into the database use the ‘create’ method and provide a dictionary containing the data you want to insert. 
```
data_to_insert = {“name”: “Fluffy”, “animal_type”: “Cat”}
insert_success = shelter.create(data_to_insert)
The insert_success variable will indicate whether the insertion was successful. 
```

Read (Query): To retrieve documents or records from the database based on specific query criteria, use the ‘read’ method and provide a query dictionary. 
```
query_criteria = {“animal_type”: “Dog”}
results = shelter.read(query_criteria)
```
The results variable will contain a list of documents that match the query criteria.

Update (Change): To update documents in the database use the ‘update’ method. Provide both a search criteria dictionary to identify the documents to update and an update data dictionary to specify the changes you want to make. 
```
search_criteria = {“name”: “Buddy”}
update_data = {“age”: 6)
num_updated = shelter.update(search_criteria, update_data)
```
The num_updated variable will indicate how many records were updated.

Delete (Remove): To remove documents from the database you must use the ‘delete’ method and provide a delete criteria dictionary.  
```
delete_criteria = {“name”: “Buddy”, “age”: 6}
num_deleted = shelter.delete(delete_criteria) 
```
The num_deleted variable will indicate how many records were deleted.


Insert:
  
![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/78a5d610-3d80-4a76-ab9e-554674e32b74)

![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/7b02d4a3-fe5b-42d6-a007-176167c12870)

# Read
![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/5df74290-7329-44c8-8970-0a2adb9e7a36)
![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/55105646-6bf5-4261-90c4-9abf061d6af6)

# Update
![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/898fe81e-95c1-4b0e-a8ef-5c1549cfa3ef)
![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/6652fb7e-303d-4e58-8cd7-29ace2c6ba99)

# Delete
![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/ff491cc1-f69e-45ad-b096-92bd8885758d)
![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/1afff672-8c65-4a15-89fc-0203a3c5daba)

# Reset Filter
![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/852023d4-16c2-4efe-bc5d-0d5da1cc0a10)

#Water Rescue Filter
![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/0865610a-ab64-41d4-84ad-d42af93fc59c)

#Mountain Rescue Filter
![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/fedad37b-80b8-402b-919c-ef3a359a759a)

# Disaster Filter
![image](https://github.com/ColeBaxendale/CRUD_Python_MONGO/assets/97856451/4895c993-c08c-4c14-a6d8-dadb347e603c)


**How do you write programs that are maintainable, readable, and adaptable? What were the advantages of working in this way? How else could you use this CRUD Python module in the future?**

Creating maintainable, readable, and adaptable programs requires clear, well-documented, and modular code. Consistent coding standards, meaningful variable names, and robust error handling are crucial. These practices simplify maintenance, enhance collaboration, and ensure the application's resilience and scalability. Moreover, using version control systems, like Git, facilitates tracking changes and supports effective team collaboration.

The advantages of such disciplined coding are significant. Not only does it reduce the time required for debugging and new feature integration, but it also makes the onboarding process for new developers smoother. The CRUD Python module used in this project exemplifies these principles. Its design allows for adaptability, making it suitable for various future applications, from data analysis to integration into larger systems, demonstrating the long-term benefits of this approach.


**How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?**

Approaching a problem as a computer scientist requires a blend of analytical thinking, creativity, and practical application. In the Grazioso Salvare project, unlike more theoretical assignments from other courses, the process began with a comprehensive analysis of the client's unique needs, emphasizing practicality and real-world functionality. The project demanded a meticulous design phase, prioritizing data integrity, security, and a user-friendly interface for the database and dashboard. This real-world scenario necessitated an iterative development process with continuous refinement, setting it apart from previous academic exercises. It underscored the importance of a client-oriented mindset, where the solution is tailored not just to meet but to exceed the client's operational requirements and strategic objectives.

For future database projects, several key strategies have been underscored. First, understanding the client's requirements is paramount, followed by designing a normalized database to ensure data integrity and efficiency. Security measures must be robust, and the system must be built with scalability in mind to accommodate growth. The user interface should be intuitive, enhancing the user's interaction with the system. Furthermore, maintaining open channels for client feedback ensures the solution remains relevant and effective. Finally, providing comprehensive documentation and training for the client ensures they can fully leverage the system's capabilities. These strategies are fundamental in delivering not just a product, but a comprehensive solution that aligns closely with the client's needs and future aspirations.


**What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?**

Computer scientists solve complex problems through the innovative application of mathematical theories, computational algorithms, and information technology. Their work matters because it drives advancements across numerous fields, making processes more efficient, data more accessible, and complex tasks more manageable. They are integral in shaping the digital world, from developing new technologies and systems that improve daily life to creating solutions that keep data secure. By leveraging their expertise in programming, data analysis, artificial intelligence, and more, computer scientists can automate processes, analyze large datasets for insights, optimize systems, and create new tools that push the boundaries of what's possible.

In the context of a company like Grazioso Salvare, the work of computer scientists can significantly enhance operational efficiency, data management, and decision-making processes. By developing a tailored database system and interactive dashboard, for instance, computer scientists enable the company to organize, track, and visualize their data in a more efficient way. This not only saves time but also provides valuable insights that were previously difficult to ascertain. A custom solution, designed with the company's specific needs and challenges in mind, ensures that every feature is relevant and adds value. For example, in this project, the dashboard could help staff quickly locate animals in need or identify trends in rescue cases, leading to more lives saved. Additionally, data-driven decision-making can spotlight areas for improvement, guide resource allocation, and inform strategic planning. Thus, the work of computer scientists not only improves current operations but also paves the way for continued growth and innovation, ensuring the company remains resilient and effective in its noble cause.




