# aws-sam-lambda-python
AWS SAMで Python3.9 ランタイムのLambda関数を作成します。

## 参考記事
下記記事を参考にしました。

https://dev.classmethod.jp/articles/sam-lambda-with-library/


## 事前準備

### 必要なファイル作成

下記階層で、フォルダやファイルを作成します。（本リポジトリの内容）

```txt
aws-sam-lambda-python
├── function
│   ├── function.py
│   └── requirements.txt
├── samconfig.toml
└── template.yaml
```


### バケット作成

AWS SAMでdeployするためには、S3にバケットが必要です。事前に作成しておきます。

```bash
$ aws s3 mb s3://test-sam-python-tochiji-2022
```

このバケット名は、`samconfig.toml` 内の `s3_bucket = "test-sam-python-tochiji-2022"` 部分で指定します。

## デプロイ方法

### 1. コードをビルドします

```bash
$ sam build

Building codeuri: /Users/XXXX/aws-sam-lambda-python/function runtime: python3.9 metadata: {} architecture: x86_64 functions: ['Function']
Running PythonPipBuilder:ResolveDependencies
Running PythonPipBuilder:CopySource

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Validate SAM template: sam validate
[*] Invoke Function: sam local invoke
[*] Test Function in the Cloud: sam sync --stack-name {stack-name} --watch
[*] Deploy: sam deploy --guided
```

### 2. コードをテストします

Dockerを利用するので、Dockerを立ち上げておく必要があります。

```bash
$ sam local invoke

Invoking function.lambda_handler (python3.9)
Image was not found.
Removing rapid images for repo public.ecr.aws/sam/emulation-python3.9
Building image.....................................................................................................................
Skip pulling image and use local one: public.ecr.aws/sam/emulation-python3.9:rapid-1.50.0-x86_64.

Mounting /Users/XXXX/aws-sam-lambda-python/.aws-sam/build/Function as /var/task:ro,delegated inside runtime container
START RequestId: e5d12f10-7915-4f43-9bc1-3bfaXXXXXXX Version: $LATEST
<Response [200]>
END RequestId: e5d12f10-7915-4f43-9bc1-3bfaXXXXXXX
REPORT RequestId: e5d12f10-7915-4f43-9bc1-3bfaXXXXXXX  Init Duration: 1.01 ms  Duration: 2490.18 ms    Billed Duration: 2491 ms        Memory Size: 128 MB    Max Memory Used: 128 MB
{"statusCode": 200, "body": "\"Hello from Lambda!\""}%     
```

求める結果なら、テスト成功です。


### 3. 関数をデプロイします

```bash
$ sam deploy
...
Successfully created/updated stack - test-sam-python-tochiji-2022 in ap-northeast-1
```

`Successfully created/updated stack` と表示されれば、成功です。
