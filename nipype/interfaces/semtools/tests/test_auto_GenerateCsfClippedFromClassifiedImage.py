# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..featurecreator import GenerateCsfClippedFromClassifiedImage


def test_GenerateCsfClippedFromClassifiedImage_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputCassifiedVolume=dict(
            argstr='--inputCassifiedVolume %s',
            extensions=None,
        ),
        outputVolume=dict(
            argstr='--outputVolume %s',
            hash_files=False,
        ),
    )
    inputs = GenerateCsfClippedFromClassifiedImage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_GenerateCsfClippedFromClassifiedImage_outputs():
    output_map = dict(outputVolume=dict(extensions=None, ), )
    outputs = GenerateCsfClippedFromClassifiedImage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
