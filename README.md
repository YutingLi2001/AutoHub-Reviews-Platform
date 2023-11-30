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
1. Start the server:
   ```
   python3 manage.py runserver
   ```
   Access the application at the associated port, appending `/djangoapp/` at the end of the URL.

2. To apply database migrations, run:
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

3. To create a superuser for admin-level operations:
   ```
   python3 manage.py createsuperuser
   ```
   Then access the admin panel by adding `/admin` to the end of the URL.

## Features
- **Branch Lookup by State**: Easily find dealership branches in any state.
- **Customer Reviews**: Read and write reviews for various branches.

## Contributing
Contributions to AutoHub Reviews are always welcome, whether it be improvements to the documentation or new functionality. Please read our contribution guidelines before starting your work.

## License
This project is forked from [IBM Developer Skills Network](https://github.com/ibm-developer-skills-network/agfzb-CloudAppDevelopment_Capstone) and is under the standard Apache 2.0 license. For more information, see the [LICENSE](LICENSE) file in the repository.

## Contact
For any queries or support, please contact me at s9ting.li@gmail.com

## Project Wiki
For detailed documentation and user guides, please visit our [Project Wiki](https://github.com/yourusername/yourrepository/wiki).
```
