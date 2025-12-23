# k8s-lakehouse-platform

## 프로젝트 개요
이 프로젝트는 Kubernetes 환경에서 데이터 엔지니어링의 핵심 흐름을
직접 구현하고 이해하기 위한 학습 중심 프로젝트입니다.

AWS S3 기반 데이터 레이크 위에 배치 데이터 파이프라인을 구축하고,
Iceberg 테이블을 통해 데이터를 관리하며,
Trino로 SQL 분석이 가능한 Lakehouse 구조를 구성합니다.
또한 Airflow를 사용해 Spark 배치 작업을 오케스트레이션하고,
실패 시 재시도(retry) 동작을 검증합니다.

본 프로젝트는 운영 환경을 그대로 재현하는 것이 아니라,
**데이터 플랫폼의 구조와 실행 흐름을 이해하는 것**을 목표로 합니다.

---

## 아키텍처 개요
데이터 흐름은 다음과 같습니다.

1. Python 기반 이벤트 데이터 생성기가 사용자 로그(JSON)를 생성하여 S3에 적재
2. Spark 배치 잡이 S3 Raw 데이터를 읽어 정제 후 Iceberg 테이블로 저장
3. Trino를 통해 Iceberg 테이블을 SQL로 조회
4. Airflow가 Spark 배치 잡을 오케스트레이션하며,
   실패 시 retry 메커니즘을 통해 재실행을 수행

모든 컴포넌트는 로컬 Kubernetes 환경에서 컨테이너로 실행됩니다.

---

## 사용 기술 스택
- Kubernetes (로컬 환경)
- AWS S3
- Apache Spark (Batch Processing)
- Apache Iceberg
- Trino
- Apache Airflow
- Python

---

## 완료 기준
아래 조건을 만족하면 프로젝트를 완료한 것으로 간주합니다.

- Spark 배치 잡을 Airflow DAG으로 실행 가능
- Iceberg 테이블이 S3에 정상적으로 생성 및 관리됨
- Trino를 통해 Iceberg 테이블 SQL 조회 가능
- Spark 잡 실패 시 Airflow retry 동작이 로그로 확인됨

---

## 참고 사항
- 로컬 Kubernetes 환경의 한계로 인해 S3 접근은 Access Key 방식으로 구성합니다.
- 운영 환경에서는 IAM Roles for Service Account(IRSA)를 사용하는 것을 전제로 설계했습니다.
- 데이터 품질 관리, 모니터링, 실시간 스트리밍(Flink)은 확장 범위로 제외했습니다.
