# prometheus

<!-- TODO Provide a high level description of the component -->


1. [operator](#operator)
1. [cluster](#cluster)


## operator

<!-- TODO Provide a description for the component operator -->

### Parameters

Component operator does not provide any parameters.


### Overlays

Component operator does not provide any overlays.


## cluster

<!-- TODO Provide a description for the component cluster -->

### Parameters

Component cluster does not provide any parameters.


### Overlays

Component cluster does not provide any overlays.



## KFdef Example

<!-- TODO Review the following generated snippet and make sure it provides a good example -->

```

- kustomizeConfig:
    repoRef:
      name: manifests
      path: prometheus/operator
  name: prometheus-operator

- kustomizeConfig:
    repoRef:
      name: manifests
      path: prometheus/cluster
  name: prometheus-cluster

```
