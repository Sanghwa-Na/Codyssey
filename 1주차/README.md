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
- [x] 권한 변경 실습
- [] Docker 설치/점검
- [] hello-world 실행
- [] Dockerfile 빌드/실행
- [] 포트 매핑 접속(2회)
- [] 바인드 마운트 반영
- [] 볼륨 영속성
- [x] Git 설정 + VSCode GitHub 연동

# 수행 로그
터미널 조작

``` 
bdn9805615@c4r2s3 Codyssey % pwd 
/Users/bdn9805615/Documents/Codyssey 
```

``` 
bdn9805615@c4r2s3 Codyssey % ls -a 
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

권한 실습

```
bdn9805615@c4r2s3 test % ls -l
total 0
-rw-r--r--  1 bdn9805615  bdn9805615   0  7 28 17:36 test.md
drwxr-xr-x  2 bdn9805615  bdn9805615  64  7 28 17:08 test3
```

```
bdn9805615@c4r2s3 test % ls -l
total 0
--w-------  1 bdn9805615  bdn9805615   0  7 28 17:36 test.md
drwxr-xr-x  2 bdn9805615  bdn9805615  64  7 28 17:08 test3
```

```
bdn9805615@c4r2s3 test % chmod -w test.md 
bdn9805615@c4r2s3 test % ls -l
total 0
----------  1 bdn9805615  bdn9805615   0  7 28 17:36 test.md
drwxr-xr-x  2 bdn9805615  bdn9805615  64  7 28 17:08 test3
```

```
bdn9805615@c4r2s3 test % chmod -r test3
bdn9805615@c4r2s3 test % ls -l
total 0
----------  1 bdn9805615  bdn9805615   0  7 28 17:36 test.md
d-wx--x--x  2 bdn9805615  bdn9805615  64  7 28 17:08 test3
bdn9805615@c4r2s3 test %  chmod -w test3
bdn9805615@c4r2s3 test % ls -l
total 0
----------  1 bdn9805615  bdn9805615   0  7 28 17:36 test.md
d--x--x--x  2 bdn9805615  bdn9805615  64  7 28 17:08 test3
```
# 권한 의미
- 소유자, 그룹, 기타 사용자
- 읽기 r=4, 쓰기 w=2, 실행 x=1
- 755 (모든, 읽기실행, 읽기실행) 소유자 모든 권한 타인은 읽고실행만, 644 (읽기쓰기, 읽기, 읽기) 소유자 읽고실행만 타인은 읽기만

# 트러블 슈팅

```
문제 : git push시 발생함 : src refspec master does not match any 
원인 : 내 정보 등록 안해서 주소 못찾는듯
해결 : git config user.name, git config user.email 등록 
```

# Git 설정 및 Github 연동

```
bdn9805615@c4r2s3 Codyssey % git config --list
credential.helper=osxkeychain
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/Sanghwa-Na/Codyssey.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
branch.main.vscode-merge-base=origin/main
user.name=Sanghwa-Na
user.email=bdn980@gmail.com
```

<img src="github.png" width="200" height="200"/>

