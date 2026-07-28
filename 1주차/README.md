# 프로젝트 목표
- 내 컴퓨터에 개발 환경 세팅하기

# 실행 환경
- OS : Sequoia 15.7.5
- Shell : zsh
- Git : 2.54
- Docker 
- vscode : 1.112.0

# 수행 체크리스트
- [x] 터미널 기본 조작 및 폴더 구성
- [] 권한 변경 실습
- [] Docker 설치/점검
- [] hello-world 실행
- [] Dockerfile 빌드/실행
- [] 포트 매핑 접속(2회)
- [] 바인드 마운트 반영
- [] 볼륨 영속성
- [x] Git 설정 + VSCode GitHub 연동

# 수행 로그

``` 
bdn9805615@c4r2s3 Codyssey % pwd 
/Users/bdn9805615/Documents/Codyssey 
```

``` bdn9805615@c4r2s3 Codyssey % ls -a 
 .		..		.git		1주차		README.md 
 ```

```
bdn9805615@c4r2s3 ~ % ls  
Desktop		Downloads	Movies		Pictures
Documents	Library		Music		Public
bdn9805615@c4r2s3 ~ % cd Documents 
```

```
bdn9805615@c4r2s3 Documents % mkdir test
bdn9805615@c4r2s3 Documents % ls
Codyssey	test
```

```
bdn9805615@c4r2s3 test % touch test.md
bdn9805615@c4r2s3 test % ls
test.md	test3
```

```
bdn9805615@c4r2s3 test % cp test.md test3
bdn9805615@c4r2s3 test % cd test3 
bdn9805615@c4r2s3 test3 % ls
test.md
```

```
bdn9805615@c4r2s3 test % mv test.md test3
bdn9805615@c4r2s3 test % ls
test3
```

```
bdn9805615@c4r2s3 test3 % cat test.md 
test%  
```

```
bdn9805615@c4r2s3 test3 % rm test.md 
bdn9805615@c4r2s3 test3 % ls
```

```
bdn9805615@c4r2s3 Documents % rm -r test2
bdn9805615@c4r2s3 Documents % ls
Codyssey	test
```