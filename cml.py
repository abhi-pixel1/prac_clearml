from argparse import ArgumentParser
from clearml import Dataset, Task



# adding command line interface, so it is easy to use
parser = ArgumentParser()
parser.add_argument('--dataset', default='aayyzz', type=str, help='Dataset ID to train on')
args = parser.parse_args()

# creating a task, so that later we could override the argparse from UI
task = Task.init(project_name='clearml_prac1', task_name='apple_data_download1')

# getting a local copy of the dataset
# dataset_folder = Dataset.get(dataset_name='apple_stock1', dataset_project='clearml_prac1').get_local_copy()
dataset_folder = Dataset.get(dataset_id=args.dataset, only_completed=False, alias=args.dataset).get_local_copy()


# go over the files in `dataset_folder` and train your model