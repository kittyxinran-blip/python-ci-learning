# Python conversion metrics: guided CI exercise

An AI-assisted starter project for learning GitHub Actions and automated tests.
The learner must run, inspect and modify it before claiming personal practice.
This is continuous integration (CI), not cloud deployment or a full CD pipeline.
No AWS account, secrets, payments or third-party Python dependencies are required.

## Files
- `metrics.py`: conversion percentage with count validation.
- `test_metrics.py`: seven tests covering ordinary, boundary and invalid inputs.
- `python-tests.yml`: workflow template. On GitHub save it at
  `.github/workflows/python-tests.yml`; it does not run from the root directory.

## Run locally
`python3 -m unittest discover -v`

## Guided learning
1. Run the workflow in your own repository and inspect the test log.
2. Add a test for 50 visitors and 5 purchases (expected 10.0 percent).
3. Observe another run. Optional: deliberately change that expected result to
   11.0, inspect the failed assertion, then restore 10.0 and rerun.
4. Record actual dates, time spent, screenshots and what you understood.
   Do not present an intentional failure as an unexpected historical problem.

This starter was generated with ChatGPT assistance. Adapt it and disclose
assistance according to your course policy. Do not claim sole authorship.

Reference: https://docs.github.com/en/actions/tutorials/build-and-test-code/python
