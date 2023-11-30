# AutoHub Reviews

## Introduction
AutoHub Reviews is a comprehensive platform designed to bring transparency and trust to the car dealership experience. It allows customers to search for dealership branches by state, view, and post reviews. Our aim is to enhance customer experience and provide valuable feedback to dealerships.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Project Wiki](#project-wiki)

## Installation
To set up AutoHub Reviews on your local machine, follow these steps:
1. Navigate to the `server` directory: `cd server/`
2. Install the required dependencies:
   ```
   python3 -m pip install -U -r requirements.txt
   ```

## Usage
After installation, here's how to run AutoHub Reviews:

- **Starting the Server:**
  Run the server using the command below. You can access the application at the associated port, appending `/djangoapp/` at the end of the URL.
  ```
  python3 manage.py runserver
  ```

- **Optional Steps:**
  These steps are independent and optional but recommended for full functionality.

  - **Applying Database Migrations:**
    To apply database migrations, use the following commands. This step helps in setting up your database schema.
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

  - **Creating a Superuser:**
    For admin-level operations, creating a superuser is advisable. Follow the steps below and then access the admin panel by adding `/admin` to the end of the URL.
    ```
    python3 manage.py createsuperuser
    ```

## Features

**AutoHub Reviews: Revolutionizing Car Dealership Experiences**

AutoHub Reviews is designed to enhance customer satisfaction and trust in our national car dealership network. With a focus on transparency and user engagement, our platform offers a variety of features catering to different user roles. Here's an overview of what AutoHub Reviews brings to the table:

### For All Users
- **Nationwide Dealership Database:** Access a comprehensive list of our branches across the United States.
- **Branch-Specific Reviews:** Read unbiased, customer-generated reviews for any dealership branch.
- **Intuitive Search Functionality:** Easily look up branches by state, ensuring quick and relevant results.
- **Emotion Analysis:** Leveraging Watson Natural Language Understanding, we analyze the sentiment behind each review to give a deeper insight into customer experiences.

### For Registered Users
- **Personalized Accounts:** Create your own account to contribute to our community.
- **Review Submission:** Share your experiences by writing reviews for any branch you've interacted with.
- **Profile Management:** Maintain and update your personal profile, keeping your interaction history at your fingertips.

### For Admin Users
- **Review Moderation:** Admins can monitor and manage customer reviews to ensure authenticity and appropriateness.
- **Data Insights:** Access detailed analytics about customer sentiments and trends across different branches.
- **Branch Management:** Update information about dealership branches, ensuring accurate and current data for users.

### Technical Architecture
- **Django Application:** Our user-friendly web interface is powered by Django, offering a seamless browsing experience.
- **User Authentication:** We ensure the security of user accounts through robust authentication mechanisms, supported by SQLite.
- **Data Management:** Car makes, models, and user credentials are securely stored in an SQLite database.
- **Cloudant NoSQL Database:** Dealership information and customer reviews are managed in Cloudant, providing scalable and flexible data storage.
- **IBM Cloud Functions:** These functions act as an intermediary between the Django application and Cloudant, enabling efficient data retrieval and submission.
- **Proxy Services:** A set of proxy services connects the Django application with IBM Cloud Functions, ensuring smooth data exchange.
- **Containerization with Docker and Kubernetes:** 
  - **Docker:** Our application components, including the Django web app and proxy services, are containerized using Docker. This ensures consistent and isolated environments for development, testing, and production.
  - **Kubernetes Orchestration:** Kubernetes manages these containers, automating deployment, scaling, and operations. This provides enhanced performance, scalability, and reliability, crucial for managing our nationwide dealership network.
  - **Combined Efficiency:** The integration of Docker and Kubernetes offers a robust containerization strategy, ensuring that our platform is agile, resilient, and capable of handling dynamic workloads with optimal resource utilization.

## Contributing
We value contributions from the community. Whether it's improving the code, fixing bugs, or enhancing documentation, all contributions are welcome!
If you're interested in contributing to AutoHub Reviews, please read our [contribution guidelines](CONTRIBUTING.md) for more information on how to get started.

## License
This project is forked from [IBM Developer Skills Network](https://github.com/ibm-developer-skills-network/agfzb-CloudAppDevelopment_Capstone) and is under the standard Apache 2.0 license. For more information, see the [LICENSE](LICENSE) file in the repository.

## Project Wiki
For detailed documentation and user guides, please visit our [Project Wiki](https://github.com/YutingLi2001/AutoHub-Reviews-Platform/wiki).
