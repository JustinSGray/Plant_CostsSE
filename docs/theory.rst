.. _theory:

Theory
------

The theory for the NREL models in this software are based directly on the work described in the reference for the NREL Cost and Scaling Model :cite:`Fingersh2006`.  The NREL Cost and Scaling Model provides a simple cost and sizing tool to estimate wind plant cost of energy based on a small number of input parameters such as rotor diameter, hub height and rated power.  The models here extract the balance of station and operational expenditure calculators from the model as stand-alone modules.

The theory for the ECN Offshore OPEX Model can be found in :cite:`ECN2012`, :cite:`Obdam2011a` and :cite:`Obdam2011b`.  This model is an external model and only an OpenMDAO wrapper for the model is provided here.


.. only:: html

    :bib:`Bibliography`

.. bibliography:: references.bib
    :style: unsrt
