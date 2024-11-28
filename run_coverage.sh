#!/bin/bash

pip install coverage
pip install coverage-badge

coverage run -m pytest
coverage-badge -o coverage.svg
