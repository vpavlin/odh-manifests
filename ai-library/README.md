# ai-library

The AI Library is an open source collection of AI components machine learning algorithms and solutions to common use cases to allow rapid prototyping.


1. [operator](#operator)
1. [cluster](#cluster)


## operator

The component operator contains the manifests which do not require cluster-admin privileges to be deployed and is mainly responsible for creating the AI Library operator deployment and roles.

### Parameters

Component operator does not provide any parameters.


### Overlays

Component operator does not provide any overlays.


## cluster

The component cluster contains manifests which require cluster-admin privileges to be deployed like CustomResourceDefinitions.

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
      path: ai-library/operator
  name: ai-library-operator

- kustomizeConfig:
    repoRef:
      name: manifests
      path: ai-library/cluster
  name: ai-library-cluster

```
