## AKS(Azure Kubernetes Service) 개요
- 관리형 Kubernetes 서비스로 컨테이너 앱 배포/관리
- 최소한의 오케스트레이션 지식으로 사용 가능
- Azure가 컨트롤 플레인 자동 관리, 복잡성 감소

## 주요 특징
- 고가용성, 확장성, 이식성 제공
- 상태 모니터링 및 유지 관리 자동화
- 실행 노드에 대해서만 비용 지불

## 주요 사용 사례
- 기존 앱 컨테이너화 마이그레이션
- 마이크로서비스 배포/관리
- 보안 DevOps 구현
- 기계학습, 데이터 스트리밍

## 핵심 기능
- ID/보안 관리, 로깅/모니터링
- 간소화된 배포, 클러스터/노드 관리
- 스토리지, 네트워킹 옵션
- 개발 도구 통합

## AKS의 클러스터

- Kubernetes 리소스의 논리적 그룹
- 컨테이너화된 애플리케이션 실행 환경
- 노드 수 조정하여 확장이 가능함, 여러 가용성 영역에 분산 가능.
- Azure 포털, CLI, API 통해서 생성 및 관리가 가능함.
- 가상 네트워크 내에서 동작하며, 내부/외부 로드 밸런서 지원

## az aks 자주 사용되는 명령어

[Azure Kubernetes Service(AKS)](https://learn.microsoft.com/en-us/cli/azure/aks?view=azure-cli-latest)에서 자주 사용되는 유용한 명령어

| 명령어 | 설명 | 예시 |
|--------|------|------|
| az aks create | AKS 클러스터 생성 | `az aks create -g MyResourceGroup -n MyCluster --node-count 3` |
| az aks get-credentials | AKS 클러스터 접속 정보 가져오기 | `az aks get-credentials -g MyResourceGroup -n MyCluster` |
| az aks scale | 노드 수 조정 | `az aks scale -g MyResourceGroup -n MyCluster --node-count 5` |
| az aks upgrade | 클러스터 버전 업그레이드 | `az aks upgrade -g MyResourceGroup -n MyCluster --kubernetes-version 1.21.0` |
| az aks show | 클러스터 정보 조회 | `az aks show -g MyResourceGroup -n MyCluster` |
| az aks nodepool add | 노드풀 추가 | `az aks nodepool add -g MyResourceGroup --cluster-name MyCluster -n mynodepool` |
| az aks update | 클러스터 설정 업데이트 | `az aks update -g MyResourceGroup -n MyCluster --enable-cluster-autoscaler` |
| az aks delete | 클러스터 삭제 | `az aks delete -g MyResourceGroup -n MyCluster` |
| az aks start | 중지된 클러스터 시작 | `az aks start -g MyResourceGroup -n MyCluster` |
| az aks stop | 클러스터 중지 | `az aks stop -g MyResourceGroup -n MyCluster` |

- AKS 클러스터의 생성, 관리, 확장, 업그레이드 등 주요 작업을 수행하는 데 필요한 기본적인 명령어들을 포함
- 각 명령어는 리소스 그룹(-g)과 클러스터 이름(-n)을 지정필요

## az aks 그외 명령어

| 명령어 | 설명 |
|--------|------|
| az aks browse | AKS 클러스터의 대시보드를 웹 브라우저로 열기 |
| az aks check-acr | AKS 클러스터에서 ACR 접근 가능 여부 확인 |
| az aks create | 새로운 AKS 클러스터 생성 |
| az aks delete | AKS 클러스터 삭제 |
| az aks disable-addons | AKS 클러스터의 애드온 비활성화 |
| az aks enable-addons | AKS 클러스터의 애드온 활성화 |
| az aks get-credentials | AKS 클러스터 접속 정보 가져오기 |
| az aks get-upgrades | AKS 클러스터의 사용 가능한 업그레이드 버전 확인 |
| az aks get-versions | 생성 가능한 AKS 버전 목록 확인 |
| az aks install-cli | kubectl 및 kubelogin 설치 |
| az aks kanalyze | 클러스터 진단 결과 표시 |
| az aks kollect | 클러스터 진단 정보 수집 |
| az aks list | AKS 클러스터 목록 조회 |
| az aks nodepool add | 노드풀 추가 |
| az aks nodepool delete | 노드풀 삭제 |
| az aks nodepool list | 노드풀 목록 조회 |
| az aks nodepool scale | 노드풀 스케일 조정 |
| az aks nodepool update | 노드풀 설정 업데이트 |
| az aks operation-abort | 진행 중인 작업 중단 |
| az aks remove-dev-spaces | Azure Dev Spaces 제거 |
| az aks rotate-certs | 클러스터 인증서 갱신 |
| az aks scale | 클러스터 노드 수 조정 |
| az aks show | 클러스터 정보 조회 |
| az aks start | 중지된 클러스터 시작 |
| az aks stop | 클러스터 중지 |
| az aks update | 클러스터 설정 업데이트 |
| az aks update-credentials | 클러스터 인증 정보 업데이트 |
| az aks upgrade | 클러스터 버전 업그레이드 |
| az aks use-dev-spaces | Azure Dev Spaces 사용 설정 |
| az aks wait | 클러스터가 특정 상태에 도달할 때까지 대기 |

- 특정 작업에 대한 자세한 사용법은 `az aks [command] --help`를 통해 확인 가능

## 가격

[AKS 가격](https://learn.microsoft.com/ko-kr/azure/aks/free-standard-pricing-tiers)
- 무료 : 추가 비용없이 개발 클러스터 또는 소규모 테스트환경, 노드가 10개 미만인 경우는 무료 제공 가능
    
## 주요 문서

- [AKS 공식문서](https://learn.microsoft.com/ko-kr/azure/aks/)
- [Azure 학습](https://learn.microsoft.com/ko-kr/azure/aks/tutorial-kubernetes-prepare-app?tabs=azure-cli)