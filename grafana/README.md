# grafana

<!-- TODO Provide a high level description of the component -->


1. [grafana](#grafana)
1. [cluster](#cluster)


## grafana

<!-- TODO Provide a description for the component grafana -->

### Parameters

Component grafana does not provide any parameters.


### Overlays

Component grafana does not provide any overlays.


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
      path: grafana/grafana
  name: grafana-grafana

- kustomizeConfig:
    repoRef:
      name: manifests
      path: grafana/cluster
  name: grafana-cluster

```
