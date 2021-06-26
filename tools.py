import os
import subprocess
import json
from config import config

cfg = config[os.environ['ENVIRONMENT']]


class CommandBuilder:
    tertiary_params = [
        '--endpoint-url {}'.format(cfg.LOCALSTACK_ENDPOINT),
        '--region {}'.format(cfg.REGION),
        '--profile {}'.format(cfg.PROFILE)
    ]
    commands = []

    def __init__(self):
        pass

    def _gen_command(self, command):
        return 'aws {} {}'.format(command, ' '.join(self.tertiary_params))

    def execute(self, command):
        command = self._gen_command(command)
        self.commands.append(command)
        try:
            os.system(command)
        except Exception as e:
            print(e)

    def output(self, command):
        try:
            return subprocess.check_output(self._gen_command(command), shell=True)
        except Exception as e:
            print(e)

    def print_execution_steps(self):
        for c in self.commands:
            print(c)


class CB(CommandBuilder):

    def __init__(self, *args, **kwargs):
        super(CommandBuilder, self).__init__(*args, **kwargs)

    # LAMBDAS
    def _list_lambdas(self):
        return self.output('lambda list-functions')

    def delete_lambdas(self):
        result = self._list_lambdas()
        if result:
            lambdas = json.loads(result)
            for function in lambdas['Functions']:
                self.execute('lambda delete-function --function-name {}'.format(function['FunctionName']))

    def rebuild_lambdas(self, lambda_details):
        for ld in lambda_details:
            self.rebuild_lambda(ld['path'], ld['package'])

    def rebuild_lambda(self, path, package):
        try:
            os.system('ls {}.zip'.format(path + package))
            os.system('rm {}.zip'.format(path + package))
        except Exception as e:
            print(e)

        try:
            os.system("cd {}venv/lib/python3.8/site-packages && \
            zip -q -r ../../../../{}.zip . && \
            cd ../../../../ && \
            zip -g {}.zip -q -r . --exclude 'venv/*' --exclude '.git*' --exclude 'migrations/*' --exclude 'README.md' --exclude 'requirements.txt'".format(
                path, package, package
            ))
        except Exception as e:
            print(e)

    def create_lambdas(self, lambda_details):
        for ld in lambda_details:
            role_arn = self._get_role_arn(ld['role'])
            self.create_lambda(ld['path'], ld['package'], ld['name'], role_arn, ld['env_vars'])

    def create_lambda(self, path, package, name, role_arn, env_vars):
        command = 'lambda create-function --function-name {} --runtime python3.8 --role {} --handler {} --zip-file fileb://{}.zip'.format(name, role_arn, 'main.lambda_handler', path + package)
        self.execute(command)

    def _get_lambda_arn(self, name):
        return json.loads(self.output('lambda get-function-configuration --function-name {}'.format(name)))['FunctionArn']

    def _get_event_source_arn(self, name):
        queue_url = json.loads(self.output('sqs get-queue-url --queue-name {}'.format(name)))['QueueUrl']
        queue_arn = json.loads(self.output('sqs get-queue-attributes --queue-url {} --attribute-names QueueArn'.format(queue_url)))['Attributes']['QueueArn']
        return queue_arn

    # REPORT
    def gen_report(self):
        messages = []

        messages.append('\nCommands Run:')
        messages.append('-------------')
        messages = messages + [c + '\n' for c in self.commands]

        messages.append('\nLambda Functions:')
        messages.append('-------------')
        result = self._list_lambdas()
        if result:
            messages.append(json.loads(result))

        print('\n\n========================')
        print('-------- Report --------')
        print('========================')
        print('%s' % '\n'.join(map(str, messages)))
        print('\n')
