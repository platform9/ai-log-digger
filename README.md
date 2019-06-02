# daaas
Data Analytics as a Service (a Hackathon 11 project) (Name to be changed)

Steps to demo:
1. Install necessary libraries (`pip install sklearn, pandas`)
2. Train the model and save it to disk (model.sav)
   `python trainer.py success_samples/ failure_samples/`
3. Predict from the log failure_test using the saved model.
   `python data_source.py failure_test`

