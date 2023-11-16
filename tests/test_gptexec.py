import pytest
import os
from gptexec import action_exec, action_updateFile, action_getFile

def test_action_exec():
    result = action_exec('echo "Hello, World!"')
    assert result['output'] == 'Hello, World!\n'

def test_action_updateFile():
    test_content = 'Test content'
    test_path = 'testfile.txt'
    # Write test content to a file
    action_updateFile(test_path, test_content)
    # Read content to verify
    with open(test_path, 'r') as file:
        content = file.read()
    # Clean up test file
    os.remove(test_path)
    # Assert test content is written correctly
    assert content == test_content

def test_action_getFile():
    test_path = 'testfile.txt'
    test_content = 'Test file content'
    # Write test content to a file
    with open(test_path, 'w') as file:
        file.write(test_content)
    # Use action to retrieve the content
    result = action_getFile(test_path)
    # Clean up test file
    os.remove(test_path)
    # Assert the content is retrieved correctly
    assert result['content'] == test_content
