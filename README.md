# AutoHub Reviews

## Introduction
AutoHub Reviews is a dynamic platform enhancing the car dealership experience through transparency and trust. It facilitates dealership searches, review posting, and offers valuable insights for both customers and dealerships.

## **Important:** Comprehensive Project Wiki
For detailed guidance and in-depth information, visit our [Project Wiki](https://github.com/YutingLi2001/AutoHub-Reviews-Platform/wiki). It's a vital resource for users and developers, providing extensive documentation on features, setup, and technical architecture.

## Table of Contents
- [Project Wiki](#project-wiki)
- [Installation](#installation)
- [Usage](#usage)
- [Running Containerized App on IBM Cloud](#running-containerized-app-on-ibm-cloud)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Wiki
The [AutoHub Reviews Project Wiki](https://github.com/YutingLi2001/AutoHub-Reviews-Platform/wiki) is the go-to resource for everything about our platform. It covers:
- **User Guides:** Tailored instructions for different user roles.
- **Developer Guide:** Technical details for setting up and contributing to the project.
- **Features:** In-depth look at our platform's features.
- **Technical Architecture:** Insight into the underlying technologies and architecture.

## Installation
Quickly set up AutoHub Reviews locally:
1. **Navigate to the Server Directory:**
   ```
   cd server/
   ```
2. **Install Dependencies:**
   ```
   python3 -m pip install -U -r requirements.txt
   ```

## Usage
How to run AutoHub Reviews:
- **Start the Server:**
  ```
  python3 manage.py runserver
  ```
- **Optional Steps:** Database migrations and superuser creation for full functionality.

## Running Containerized App on IBM Cloud
Deploy AutoHub Reviews on IBM Cloud with these steps:
1. **Containerize the App:** Ensure the app is packaged with Docker.
2. **Use IBM Cloud CLI:** Set up container registry and Kubernetes services.
3. **Deploy:** Launch the app using Kubernetes on IBM Cloud.

For detailed deployment instructions, check out our [Containerization and Deployment Guide using IBM Cloud](https://github.com/YutingLi2001/AutoHub-Reviews-Platform/wiki/Developer-Guide/#containerization-and-deployment-guide-using-ibm-cloud)

## Features
AutoHub Reviews offers comprehensive features for users and administrators:
- **For All Users:** Nationwide dealership database, branch-specific reviews, intuitive search.
- **For Registered Users:** Personalized accounts, submit reviews.
- **For Admin Users:** Data insights.
- **Technical Architecture:** Robust and scalable backend powered by Django, SQLite, Cloudant NoSQL, IBM Cloud Functions, Docker, and Kubernetes.

## Contributing
Contributions are welcome! Check our [contribution guidelines](CONTRIBUTING.md) for more information.

## License
This project is under the Apache 2.0 license. For details, see [LICENSE.md](LICENSE.md).


