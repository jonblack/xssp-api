import re

from flask_wtf import Form
from wtforms.fields import FileField, SelectField, TextAreaField, TextField
from wtforms.validators import length, Regexp

from xssp_rest.frontend.validators import NotRequiredIfOneOf


RE_PDB_ID = re.compile(r"^[0-9a-zA-Z]{4}$")
RE_SEQ = re.compile(r"^[XARNDCEQGHILKMFPSTWYV]+$")


class XsspForm(Form):
    input_type = SelectField(u'Input',
                             choices=[('pdb_id', 'PDB code'),
                                      ('pdb_redo_id', 'PDB_REDO code'),
                                      ('pdb_file', 'PDB file'),
                                      ('sequence', 'Sequence')])
    output_type = SelectField(u'Output',
                              choices=[('dssp', 'DSSP'),
                                       ('hssp_hssp', 'HSSP'),
                                       ('hssp_stockholm', 'HSSP (Stockholm)')])
    pdb_id = TextField(u'PDB code', [NotRequiredIfOneOf(['sequence', 'file_']),
                                     Regexp(regex=RE_PDB_ID)])
    sequence = TextAreaField(u'Sequence', [
        NotRequiredIfOneOf(['pdb_id', 'file_']),
        Regexp(RE_SEQ,
               message='Can only contain residues from ' +
                       'the set "ACDEFGHIKLMNPQRSTVWXY"'),
        length(min=25,
               message='Must be at least 25 residues long.')
    ])
    file_ = FileField(u'File', [NotRequiredIfOneOf(['pdb_id', 'sequence'])])