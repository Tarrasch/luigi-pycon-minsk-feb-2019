import luigi
import time

class ParentTask(luigi.Task):
    def requires(self):
        return [ChildTask(my_param='4+6'), ChildTask(my_param='len("Hello world")')]

    def run(self):
        acc = 0
        for target in self.input():
            with target.open() as fd:
                acc += int(fd.read())

        with self.output().open('w') as fd:
            fd.write(str(acc))

    def output(self):
        return luigi.LocalTarget('/tmp/presentation/final_result')


class ChildTask(luigi.Task):
    my_param = luigi.Parameter()

    def run(self):
        with self.output().open('w') as fd:
            fd.write(str(eval(self.my_param)))
            time.sleep(30)

    def output(self):
        return luigi.LocalTarget('/tmp/presentation/' + self.my_param)



