import importlib.util,sys,os
sys.path.insert(0,'temp')
os.chdir('temp')
print(os.getcwd())
spec = importlib.util.spec_from_file_location("Run", 'Run.pyc')
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)