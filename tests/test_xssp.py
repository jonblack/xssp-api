from mock import patch
from nose.tools import eq_, ok_, raises

from xssp_rest.services.xssp import (XsspStrategyFactory, PdbIdStrategy,
                                     PdbRedoIdStrategy, PdbContentStrategy,
                                     SequenceStrategy)


def test_xssp_strategy_factory():
    strategy = XsspStrategyFactory.create('pdb_id', 'hssp_hssp')
    ok_(isinstance(strategy, PdbIdStrategy))
    strategy = XsspStrategyFactory.create('pdb_redo_id', 'hssp_hssp')
    ok_(isinstance(strategy, PdbRedoIdStrategy))
    strategy = XsspStrategyFactory.create('pdb_file', 'hssp_hssp')
    ok_(isinstance(strategy, PdbContentStrategy))
    strategy = XsspStrategyFactory.create('sequence', 'hssp_hssp')
    ok_(isinstance(strategy, SequenceStrategy))


@raises(ValueError)
def test_xssp_strategy_factory_unexpected_input_type():
    XsspStrategyFactory.create('unexpected', 'hssp_hssp')


@patch('xssp_rest.tasks.get_task')
def test_pdb_id_strategy_hssp(mock_get_task):
    mock_get_task.return_value.__name__ = 'mock_task'
    mock_get_task.return_value.delay.return_value.id = '12345'

    strategy = PdbIdStrategy('hssp_hssp')
    result_id = strategy('1crn')
    mock_get_task.return_value.delay.assert_called_once_with('1crn',
                                                             'hssp_hssp')
    eq_(result_id, '12345')


@patch('xssp_rest.tasks.get_task')
def test_pdb_id_strategy_dssp(mock_get_task):
    mock_get_task.return_value.__name__ = 'mock_task'
    mock_get_task.return_value.delay.return_value.id = '12345'

    strategy = PdbIdStrategy('dssp')
    result_id = strategy('1crn')
    mock_get_task.return_value.delay.assert_called_once_with('1crn')
    eq_(result_id, '12345')


@raises(ValueError)
def test_pdb_redo_id_strategy_hssp():
    strategy = PdbRedoIdStrategy('hssp_hssp')
    strategy('1crn')


@patch('xssp_rest.tasks.get_task')
def test_pdb_redo_id_strategy_dssp(mock_get_task):
    mock_get_task.return_value.__name__ = 'mock_task'
    mock_get_task.return_value.delay.return_value.id = '12345'

    strategy = PdbRedoIdStrategy('dssp')
    result_id = strategy('1crn')
    mock_get_task.return_value.delay.assert_called_once_with('1crn')
    eq_(result_id, '12345')


@patch('xssp_rest.tasks.get_task')
def test_pdb_file_strategy_hssp(mock_get_task):
    mock_get_task.return_value.__name__ = 'mock_task'
    mock_get_task.return_value.delay.return_value.id = '12345'

    strategy = PdbContentStrategy('hssp_hssp')
    result_id = strategy('1crn')
    mock_get_task.return_value.delay.assert_called_once_with('1crn',
                                                             'hssp_hssp')
    eq_(result_id, '12345')


@patch('xssp_rest.tasks.get_task')
def test_pdb_file_strategy_dssp(mock_get_task):
    mock_get_task.return_value.__name__ = 'mock_task'
    mock_get_task.return_value.delay.return_value.id = '12345'

    strategy = PdbContentStrategy('dssp')
    result_id = strategy('1crn')
    mock_get_task.return_value.delay.assert_called_once_with('1crn')
    eq_(result_id, '12345')


@patch('xssp_rest.tasks.get_task')
def test_sequence_strategy_hssp(mock_get_task):
    mock_get_task.return_value.__name__ = 'mock_task'
    mock_get_task.return_value.delay.return_value.id = '12345'

    strategy = SequenceStrategy('hssp_hssp')
    result_id = strategy('1crn')
    mock_get_task.return_value.delay.assert_called_once_with('1crn',
                                                             'hssp_hssp')
    eq_(result_id, '12345')


@raises(ValueError)
def test_sequence_strategy_dssp():
    strategy = SequenceStrategy('dssp')
    strategy('1crn')