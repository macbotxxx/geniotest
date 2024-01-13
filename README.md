## Geniotest - P2P Money Transfer System
Geniotest is an innovative peer-to-peer (P2P) money transfer system designed to facilitate seamless financial transactions among friends and family members. Developed by Michael Assanama, Geniotest leverages modern technologies to create a secure, efficient, and user-friendly platform for sending and receiving money.

## Key Features
1. Peer-to-Peer Transactions
Geniotest simplifies the process of sending money directly between users, eliminating the need for intermediaries and providing a direct and personalized financial exchange experience.

2. User-Friendly Interface
The platform boasts an intuitive and user-friendly interface, making it easy for users of all technical backgrounds to navigate and utilize its features effortlessly.

3. Security and Privacy
Geniotest prioritizes the security and privacy of its users. Utilizing robust encryption protocols, the platform ensures that financial transactions and sensitive user information remain confidential and protected.

4. Fast and Efficient
With Geniotest, users can enjoy quick and efficient money transfers, reducing the time it takes for funds to reach their intended recipients. The platform leverages cutting-edge technologies to optimize transaction speed.

5. Integration with Redis
Geniotest harnesses the power of Redis for efficient caching, enhancing overall system performance and responsiveness. Redis plays a crucial role in ensuring that frequently accessed data is readily available, contributing to a smoother user experience.

6. Asynchronous Task Handling with Celery
To further enhance scalability and responsiveness, Geniotest utilizes Celery for asynchronous task handling. This enables the platform to efficiently manage background tasks, ensuring that users can perform various actions without experiencing delays.

## Getting Started
Before using Geniotest, ensure you have the required dependencies installed:

Install Redis: Follow the instructions in the README to set up and run the Redis server.
Install Celery: Use the provided command to install Celery.
Run Geniotest: Follow the steps outlined in the README to start the Geniotest Django project and access the local development server.
## About the Author
Geniotest is the brainchild of Michael Assanama, a visionary developer dedicated to creating solutions that simplify and enhance everyday experiences. Connect with Michael on GitHub and explore more about his projects and contributions.

Geniotest aims to redefine P2P money transfers, providing a secure, efficient, and enjoyable way for users to send and receive money within their trusted circles.
## Prerequisites

Before running the Geniotest project, you need to have Redis and Celery installed. Follow the instructions below to set up your environment.

### Install Redis

1. **Linux:**
   - Ubuntu:
     ```bash
     sudo apt-get update
     sudo apt-get install redis-server
     ```
   - Fedora:
     ```bash
     sudo dnf install redis
     ```
   - Other distributions: Refer to your distribution's package manager.

2. **Mac:**
   ```bash
   brew install redis

3. **Install Celery:**
   ```bash
   pip install celery

4. **Running Redis:**
   ```bash
   redis-server
   ```
   - Start the Redis server using the following command.
  
5. **Running Celery:**
   ```bash
   python3 -m celery -A config worker -l info
   ```
   - To run Celery, use the following command:

6. **Running the Django Project:**
   ```bash
   python manage.py runserver
   ```
   - Make sure you have Python and Django installed. If not, install Django using:
   - Visit http://127.0.0.1:8000/ to access the local development server.
  
  # API Documentation
  Access the API documentation at http://127.0.0.1:8000/documentation for details on available endpoints and usage.


