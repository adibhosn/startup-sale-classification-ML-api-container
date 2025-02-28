# Future-Launch  
**Startup Sale Prediction using Machine Learning**  

This project was developed based on a selection process for a study group called **LAPES**  
(available at: [LAPES GitHub](https://github.com/lapes-engenharia-de-software/.github/blob/main/profile/ps-lapes-2024.md))  

This project uses a dataset of startups to predict whether a startup will be acquired or not. The main goal is to analyze the factors that influence a startup’s success and build a Machine Learning model capable of predicting this success based on specific characteristics.  

To create a graphical interface, a web application was developed using **Flask** as the backend (API) and **Streamlit** as the frontend. The project allows users to visualize insights through graphs and make personalized predictions, all orchestrated with **Docker**.  

## Project Structure  

- **api/**: Files related to the Flask API.  
- **streamlit/**: Code related to the front-end with Streamlit.  
- **docker-compose.yml**: File for Docker container orchestration.  
- **requirements.txt**: Project dependencies.  
- **Dockerfile**: File to build the Docker image.  

## How to Run the Project  

### 1. Clone the repository:     
   ```bash
   git clone https://github.com/Adibhosn/Future-Launch.git
   ```
### 2. Navigate to the project directory:
```bash
 cd Future-Launch
```
### 3. Build and start the containers using Docker Compose:
```bash
docker-compose up --build
```
### 4. Access the applications:
```bash
http://localhost:8501/
```


