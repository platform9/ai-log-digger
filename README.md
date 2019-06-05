# daaas
AI Log Digger
(A Hackathon 11 Project)

Steps to demo:
1. Install necessary libraries (`pip install sklearn, pandas`)
2. Train the model and save it to disk (model.sav)
   `python trainer.py success_logs/ failure_logs/`
3. Predict from the test log using the saved model.
   `python data_source.py test_log/qbert.log`


