# mangum-sam-quickstart

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- hello_world - Code for the application's Lambda function. Basically a normal FastAPI app, with a mangum wrapper.
- template.yaml - A template that defines the application's AWS resources. No security is included, if deployed as is your API will be public.

## API Gateway Lambda Proxy Integration

The real magic is here, this passes any request through to the lambda we've created, with mangum/FastAPI running inside. New routes just work, like we'd expect with a container or similar. Just modify the routes in `app.py` to fit your usecase!

```yaml
Events:
  HelloWorld:
    Type: Api
    Properties:
      Path: /{proxy+}
      Method: ANY
```

Thanks to [alexharv074 for the blog post](https://alexharv074.github.io/2019/03/31/introduction-to-sam-part-iii-adding-a-proxy-endpoint-and-cors-configuration.html) that showed me this undocumented feature!

## Deploying

[Install the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

Then:

```bash
sam build -u
sam deploy --guided
```

## Local development

Install the main folder requirements, and run app.py.
