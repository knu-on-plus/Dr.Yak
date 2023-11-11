# [2023 대구를 빛내는 SW 해커톤] 

![Header](http://capsule-render.vercel.app/api?type=rect&color=auto&height=200&section=header&text=Team%20Dr.%20Yak&fontSize=80&fontAlignY=&animation=twinkling)

<details>
<summary>보고서 양식</summary>
<div markdown="1">       

- 팀명
  
  - 약박사님을 아세요?

- 제출 타입 및 주제
  
  - S타입

- 프로젝트 한 줄 설명
  
  - AI기반의 노년층 대상 약 종류 및 복용 방법 정보 제공 어시스턴트

- 프로젝트에 활용된 기술
  
  - PaddleOCR 인공지능 모델 활용 / TTS / 

- 시연 영상
  
  - URL
    

</div>
</details>


## 1. 주제
- __약박사 (Dr. YAk)__
    - AI 기반 노년층 대상 Drug Assistant


## 2. 핵심 내용
- __핵심 내용__

    - _**노년층**이 **약의 종류와 복용 방법** 등에 대한 정보를 쉽게 이해하고 접근할_ 수 있도록 도와줌

    - __OCR(Optical Character Recognition)__ 모델과 __TTS(Text-To-Speak)__ 를 활용해 사용자는 약의 사진을 _카메라로 찍어 입력하고_, 해당 약에 대한 이름과 복용 방법에 대한 상세 정보를 획득 할 수 있음


    - 기술 스택

        <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"></a> <a href="https://www.w3schools.com/html/"><img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"></a> <a href="https://javascript.info/"><img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"></a> <a href="https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html"><img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"></a> <a href="https://www.w3schools.com/css/"><img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"></a>

    #### 예상 UI Prototype

    <a href="./Images/figure1.png"><img src="./Images/figure1.png"></a>

***

- __기술 구현 및 기능 프로세스 설명__

    ### __Framework__

    <a href="./Images/figure1.png"><img src="./Images/figure2.png"></a>

    ### __Process__

1. 촬영된 사진을 OCR 인공지능 기술을 통해 뒷면의 모든 텍스트 인식

2. 인식된 텍스트 뭉치에서 Google Bard 자연어처리 모델을 이용해 약제 이름 추출

3. 약제 정보 데이터베이스에서 추출된 텍스트와 유사도가 높은 약제 검색

4. 데이터베이스에 있는 약의 이름, 복용 방법, 주의 사항을 TTS 기술을 통해 음성으로 안내

5. 수집된 이미지로 구축한 데이터셋을 통해 알약에 대한 분류기(Deep Learning based - Classification model) 학습



## 3. 제안 배경
1. **노령화 사회의 현실**

    - 한국의 노령화: 2022년 기준 65세 이상 고령자 비율이 16% 이상

    - 전 세계적인 노령화 추세: 2050년까지 65세 이상 인구가 2배 이상 증가 예상

2. **노년층의 의약품 복용률**

    - 노년층은 평균적으로 만성 질환 등으로 인해 여러 종류의 약을 먹는 경우가 많고, 이에 따라 약간의 혼동이나 잘못된 복용이 발생하기 쉬움

3. **노년층의 의약품 인식 문제점**

    - 의약품 포장의 작은 글씨로 인한 정보 인식 어려움

    - 또한, 노년층은 디지털 정보에 접근하는 데 있어 장벽을 느낄 수 있어서 약에 대한 올바른 정보를 얻기 어려울 수 있음

4. **알약 보관 방식**

    - 주로 알약을 보관할 때 약에 대한 상세 정보를 포함하는 상자를 제외하고 은박 알약 포장 형태의 상태로 보관함

    - 해당 보관함에 담은 상태로 알약이 어떤 기능을 위한 것인지 헷갈리는 상황이 생김


        #### 보관 방식의 예시
        <a href="./Images/figure3.png"><img src="./Images/figure3.png"></a>  

## 4. 사업화 방안 및 기대 효과
- 사업화 방안

    - 병원/약국 파트너십

        - 협력 병원이나 약국과의 파트너십을 구축하여 앱을 홍보하고, 해당 기관에서 추천하는 약에 대한 정보 서비스를 제공함

    - 의약품 데이터베이스 구축 및 판매

        - 의약품 포장재 사진 이미지를 확보하여 의약품 데이터베이스를 구축하여 의료, 의약계 수요자에게 판매

    - 정부 기관과의 연계

        - 사회 복지 서비스에 관한 기술로 활용 가능
    

***

- 사회 파급(효과)

    - 접근성 향상을 통한 노년층의 약 복용 안전성 향상

        - 약에 대한 정확한 정보 제공을 통해 잘못된 복용이나 부작용 발생의 위험을 줄일 수 있음

        - 디지털 장벽을 낮추는 직관적인 앱 디자인을 통해 노년층의 의약품 정보 접근성을 향상함

    - 의료 서비스와의 연계

        - 병원이나 약국과의 협력을 통해 사용자에게 추가적인 의료 서비스 정보 제공이 가능함

    - 사용자 생활의 편리성 증대

        - 의약품 복용 정보를 쉽게 확인하여 일상에서의 편의성 제공

    - 시장점유율 확대 및 브랜드 가치 상승

        - 타겟 시장을 노년층뿐만 아니라 저시력자 및 약에 대한 지식이 부족한 복용자까지 확장하여 사용자층 확대

    - 사회적 가치 창출

        - 노년층과 저시력자의 생활 품질 향상을 통한 사회적 책임 수행

이런 방식으로 구축된 앱은 _**노년층의 의약품 복용 안전성과 편의성을 향상**_ 하는 동시에 다양한 사업 모델을 통해 _**경제적 이익**도 추구_ 할 수 있을 것임

## 5. Contribute
<div align="center"> We love your input!</div>


<div align="center"><a href="https://github.com/aicoss-wim-team/Dr.-Hong/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=aicoss-wim-team/Dr.-Hong" />
</a></div>
