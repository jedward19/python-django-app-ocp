<p align="center">
    <a href="https://cloud.ibm.com">
        <img src="https://my1.digitalexperience.ibm.com/8304c341-f896-4e04-add0-0a9ae02473ba/dxdam/2d/2d559197-6763-4e47-a2cb-8f54c449ff26/ibm-cloud.svg" height="100" alt="IBM Cloud">
    </a>
</p>


<p align="center">
    <a href="https://cloud.ibm.com">
    <img src="https://img.shields.io/badge/IBM%20Cloud-powered-blue.svg" alt="IBM Cloud">
    </a>
    <img src="https://img.shields.io/badge/platform-django-lightgrey.svg?style=flat" alt="platform">
    <img src="https://img.shields.io/badge/license-Apache2-blue.svg?style=flat" alt="Apache 2">
</p>


# Create and deploy a Python Django application

> We have applications available for [Node.js Express](https://github.com/IBM/node-express-app), [Go Gin](https://github.com/IBM/go-gin-app), [Python Flask](https://github.com/IBM/python-flask-app), [Python Django](https://github.com/IBM/python-django-app), [Java Spring](https://github.com/IBM/java-spring-app), [Java Liberty](https://github.com/IBM/java-liberty-app), [Swift Kitura](https://github.com/IBM/swift-kitura-app), [Android](https://github.com/IBM/android-app), and [iOS](https://github.com/IBM/ios-app).

In this sample application, you will create a web application using Django to serve web pages in Python, complete with standard best practices, including a health check.

This app contains an opinionated set of files for web serving:

- `app/templates/index.html`
- `staticfiles/js/bundle.js`
- `staticfiles/css/default.css`

## Steps

You can [build it locally](#building-locally) by cloning this repo first. Once your app is live, you can access the `/health` endpoint to build out your cloud native application.


### Building Locally

To get started building this application locally, you can either run the application natively or use the [IBM Cloud Developer Tools](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started) for containerization and easy deployment to IBM Cloud.

#### Native Application Development

* Install [Python](https://www.python.org/downloads/)

Running Django applications has been simplified with a `manage.py` file to avoid dealing with configuring environment variables to run your app. From your project root, you can download the project dependencies with:

```bash
pipenv install
pipenv shell
```

To run your application locally:

```bash
python manage.py start
```

Your application will be running at `http://localhost:3000`.  You can access the `/health` endpoint at the host. You can also verify the state of your locally running application using the Selenium UI test script included in the `scripts` directory.

##### Debugging locally
To debug a `django` project run `python manage.py runserver` with DEBUG set to True in `settings.py` to start a native django development server. This comes with the Django's stack-trace debugger, which will present runtime failure stack-traces. For more information, see [Django's documentation](https://docs.djangoproject.com/en/2.0/ref/settings/).


#### Running via Docker

1. Docker **running**
1. Build Docker Image

    ```sh
    docker build --pull --rm -f "Dockerfile" -t pythondjangoapp:latest "."
    ```

1. Run Docker Image

    ```sh
    docker run --rm -d  -p 3000:3000/tcp pythondjangoapp:latest
    ```

1. Open browser to http://localhost:3000


## License

This sample application is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)
