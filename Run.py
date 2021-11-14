import os,importlib.util
def run(dir):
	os.chdir(dir)
	spec = importlib.util.spec_from_file_location("Run", 'Run.pyc')
	foo = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(foo)