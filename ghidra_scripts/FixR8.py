from ghidra.app.util.datatype import DataTypeSelectionDialog
from ghidra.framework.plugintool import PluginTool
from ghidra.program.model.data import DataType
from ghidra.program.model.data import DataTypeManager
from ghidra.util.data.DataTypeParser import AllowedDataTypes
from ghidra.program.model.listing import ParameterImpl
from ghidra.program.model.listing import Function
from ghidra.program.model.symbol import SourceType

fn = getFunctionContaining(currentAddress)
assert fn is not None

 
tool = state.getTool()
dtm = currentProgram.getDataTypeManager()
selectionDialog = DataTypeSelectionDialog(tool, dtm, -1, AllowedDataTypes.FIXED_LENGTH)
tool.showDialog(selectionDialog)
dataType = selectionDialog.getUserChosenDataType()
if dataType is not None:
	reg = currentProgram.getRegister('x8')
	outParam = ParameterImpl('out', dataType, reg, currentProgram)
	params = list(fn.parameters)
	params[:0] = [outParam]
	fn.updateFunction(None, None, params, Function.FunctionUpdateType.CUSTOM_STORAGE, False, SourceType.USER_DEFINED)


