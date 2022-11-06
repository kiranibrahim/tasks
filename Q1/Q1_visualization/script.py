layers = QgsProject.instance().mapLayersByName('pakistan')
layer = QgsVectorLayer(layers[0].dataProvider().dataSourceUri(), '', 'org')
caps = layer.dataProvider().capabilities()

if caps & qgsvectordataprovider.Addfeatures:
    feat= qgsfeature(layers.fields())
    feat.setattributes([0, 'add programatically'])
    feat.setgeometry(qgsgeometry.frompointXY(qgspointXY(25.1313, 62.3250)))
    res, outfeats = layer.dataproviders().addfeatures([feat])