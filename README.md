# Flask_landingpage_project
I am learning web programming (specifically Python and Flask) by building a simple landing page with a subscription form.

The webpage displays a simple subscription form. When the visitor of the page enters information in the **'Name'** and **'Email'** fields, providing their name and email, and clicks the **'Subscribe'** button, the entered data is saved in the `user_data.csv` file. Subsequently, the **'Thank you'** page is displayed.

To run the program:
#### 1. Create a virtual environment. (Recommended)
After downloading the files on your computer, open the terminal and navigate to the `Flask_landingpage_project-main` directory.
Run the following command to create a virtual environment:
```bash
python -m venv venv
```
Run this command to activate the virtual environment:
```bash
source venv/bin/activate
```

#### 2. Install the dependencies.
```bash
pip install -r requirements.txt
```

#### 3. Run the development server.
```bash
python app.py runserver
```
Now the app is running.
You can open the browser and type the address of the page:
`http://localhost:5000` or `http://127.0.0.1:5000/`

