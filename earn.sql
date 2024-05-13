PGDMP  !    5                |            ebay    16.2    16.2 :    M           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            N           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            O           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            P           1262    16657    ebay    DATABASE     f   CREATE DATABASE ebay WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
    DROP DATABASE ebay;
                postgres    false            �            1259    16677    brands    TABLE     �   CREATE TABLE public.brands (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    image character varying(255) DEFAULT '/media/default.png'::character varying
);
    DROP TABLE public.brands;
       public         heap    postgres    false            �            1259    16676    brands_id_seq    SEQUENCE     �   CREATE SEQUENCE public.brands_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.brands_id_seq;
       public          postgres    false    220            Q           0    0    brands_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.brands_id_seq OWNED BY public.brands.id;
          public          postgres    false    219            �            1259    16670 
   categories    TABLE     }   CREATE TABLE public.categories (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    parend_id integer
);
    DROP TABLE public.categories;
       public         heap    postgres    false            �            1259    16669    categories_id_seq    SEQUENCE     �   CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.categories_id_seq;
       public          postgres    false    218            R           0    0    categories_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;
          public          postgres    false    217            �            1259    16707    order_items    TABLE     �   CREATE TABLE public.order_items (
    id bigint NOT NULL,
    order_id bigint NOT NULL,
    product_id bigint NOT NULL,
    qty integer DEFAULT 1 NOT NULL,
    subtotal numeric
);
    DROP TABLE public.order_items;
       public         heap    postgres    false            �            1259    16706    order_items_id_seq    SEQUENCE     {   CREATE SEQUENCE public.order_items_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.order_items_id_seq;
       public          postgres    false    226            S           0    0    order_items_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.order_items_id_seq OWNED BY public.order_items.id;
          public          postgres    false    225            �            1259    16697    orders    TABLE     )  CREATE TABLE public.orders (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    delivery_address character varying(1000),
    delivery_phone character varying(25),
    status character varying(100) DEFAULT 'cart'::character varying NOT NULL,
    total numeric NOT NULL,
    creat_at date
);
    DROP TABLE public.orders;
       public         heap    postgres    false            �            1259    16696    orders_id_seq    SEQUENCE     v   CREATE SEQUENCE public.orders_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.orders_id_seq;
       public          postgres    false    224            T           0    0    orders_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders.id;
          public          postgres    false    223            �            1259    16687    products    TABLE     >  CREATE TABLE public.products (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    image character varying(255) DEFAULT '/media/default.png'::character varying,
    description text,
    price numeric NOT NULL,
    status boolean NOT NULL,
    brend_id integer,
    categories_id integer NOT NULL
);
    DROP TABLE public.products;
       public         heap    postgres    false            �            1259    16686    products_id_seq    SEQUENCE     x   CREATE SEQUENCE public.products_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.products_id_seq;
       public          postgres    false    222            U           0    0    products_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;
          public          postgres    false    221            �            1259    16659    users    TABLE     �  CREATE TABLE public.users (
    id bigint NOT NULL,
    login character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100),
    address character varying(1000),
    phone character varying(25) NOT NULL,
    email character varying(100),
    birth_date date,
    gender character varying(100) DEFAULT 'man'::character varying,
    status boolean DEFAULT false
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    16658    users_id_seq    SEQUENCE     u   CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public          postgres    false    216            V           0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public          postgres    false    215            �           2604    16680 	   brands id    DEFAULT     f   ALTER TABLE ONLY public.brands ALTER COLUMN id SET DEFAULT nextval('public.brands_id_seq'::regclass);
 8   ALTER TABLE public.brands ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220            �           2604    16673    categories id    DEFAULT     n   ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);
 <   ALTER TABLE public.categories ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217    218            �           2604    16710    order_items id    DEFAULT     p   ALTER TABLE ONLY public.order_items ALTER COLUMN id SET DEFAULT nextval('public.order_items_id_seq'::regclass);
 =   ALTER TABLE public.order_items ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225    226            �           2604    16700 	   orders id    DEFAULT     f   ALTER TABLE ONLY public.orders ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);
 8   ALTER TABLE public.orders ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    224    224            �           2604    16690    products id    DEFAULT     j   ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);
 :   ALTER TABLE public.products ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    222    222            �           2604    16662    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215    216            D          0    16677    brands 
   TABLE DATA           1   COPY public.brands (id, name, image) FROM stdin;
    public          postgres    false    220   �A       B          0    16670 
   categories 
   TABLE DATA           9   COPY public.categories (id, name, parend_id) FROM stdin;
    public          postgres    false    218   )B       J          0    16707    order_items 
   TABLE DATA           N   COPY public.order_items (id, order_id, product_id, qty, subtotal) FROM stdin;
    public          postgres    false    226   �B       H          0    16697    orders 
   TABLE DATA           h   COPY public.orders (id, user_id, delivery_address, delivery_phone, status, total, creat_at) FROM stdin;
    public          postgres    false    224   �B       F          0    16687    products 
   TABLE DATA           h   COPY public.products (id, name, image, description, price, status, brend_id, categories_id) FROM stdin;
    public          postgres    false    222   @C       @          0    16659    users 
   TABLE DATA           ~   COPY public.users (id, login, password, first_name, last_name, address, phone, email, birth_date, gender, status) FROM stdin;
    public          postgres    false    216   �D       W           0    0    brands_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.brands_id_seq', 2, true);
          public          postgres    false    219            X           0    0    categories_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.categories_id_seq', 5, true);
          public          postgres    false    217            Y           0    0    order_items_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.order_items_id_seq', 1, false);
          public          postgres    false    225            Z           0    0    orders_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.orders_id_seq', 3, true);
          public          postgres    false    223            [           0    0    products_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.products_id_seq', 3, true);
          public          postgres    false    221            \           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 2, true);
          public          postgres    false    215            �           2606    16685    brands brands_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.brands
    ADD CONSTRAINT brands_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.brands DROP CONSTRAINT brands_pkey;
       public            postgres    false    220            �           2606    16675    categories categories_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public            postgres    false    218            �           2606    16715    order_items order_items_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.order_items DROP CONSTRAINT order_items_pkey;
       public            postgres    false    226            �           2606    16705    orders orders_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_pkey;
       public            postgres    false    224            �           2606    16695    products products_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public            postgres    false    222            �           2606    16668    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    216            �           1259    16738    brand_id    INDEX     A   CREATE INDEX brand_id ON public.products USING btree (brend_id);
    DROP INDEX public.brand_id;
       public            postgres    false    222            �           1259    16727    brend_id    INDEX     A   CREATE INDEX brend_id ON public.products USING btree (brend_id);
    DROP INDEX public.brend_id;
       public            postgres    false    222            �           1259    16721    categoriy_id    INDEX     H   CREATE INDEX categoriy_id ON public.categories USING btree (parend_id);
     DROP INDEX public.categoriy_id;
       public            postgres    false    218            �           1259    16750    order_id    INDEX     D   CREATE INDEX order_id ON public.order_items USING btree (order_id);
    DROP INDEX public.order_id;
       public            postgres    false    226            �           1259    16756 
   product_id    INDEX     H   CREATE INDEX product_id ON public.order_items USING btree (product_id);
    DROP INDEX public.product_id;
       public            postgres    false    226            �           1259    16744    user_id    INDEX     =   CREATE INDEX user_id ON public.orders USING btree (user_id);
    DROP INDEX public.user_id;
       public            postgres    false    224            �           2606    16716 $   categories categories_parend_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_parend_id_fkey FOREIGN KEY (parend_id) REFERENCES public.categories(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 N   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_parend_id_fkey;
       public          postgres    false    3483    218    218            �           2606    16745 %   order_items order_items_order_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.orders(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 O   ALTER TABLE ONLY public.order_items DROP CONSTRAINT order_items_order_id_fkey;
       public          postgres    false    224    3492    226            �           2606    16751 '   order_items order_items_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(id) NOT VALID;
 Q   ALTER TABLE ONLY public.order_items DROP CONSTRAINT order_items_product_id_fkey;
       public          postgres    false    3490    222    226            �           2606    16739    orders orders_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 D   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_user_id_fkey;
       public          postgres    false    224    3481    216            �           2606    16733    products products_brend_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_brend_id_fkey FOREIGN KEY (brend_id) REFERENCES public.brands(id) ON UPDATE SET NULL ON DELETE SET NULL NOT VALID;
 I   ALTER TABLE ONLY public.products DROP CONSTRAINT products_brend_id_fkey;
       public          postgres    false    220    222    3486            �           2606    16728 $   products products_categories_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_categories_id_fkey FOREIGN KEY (categories_id) REFERENCES public.categories(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 N   ALTER TABLE ONLY public.products DROP CONSTRAINT products_categories_id_fkey;
       public          postgres    false    222    3483    218            D   7   x�3�t,(�I���MM�L�OIMK,�)�+�K�2�N�-.�K�IC�`�=... n��      B   I   x�3�t�I�.)����.���2�tK,����q�9��J�&��y�Ŝ�\��~��%�I��� n� 5      J   1   x�3�4�4bC#c�2�p9�LM�|cNc*o��@b���� o
9      H   m   x�=��@0���S�%��ۢ/a!&�T�HJZo���M�}�}��� ���<���[�W珤CjLe�T�Jf��Z#X�ϗ`4K�pm����9W؝?����Lqޕ�      F   ;  x�eQak�0�����4Z�6����S��ns�A�C��kRE�b�U�|8x�{��]�pm�j<&�Z�%��`�.Ղ|��H��di�ǔ>O�߀�%� ��>���	I�	�Q��?�S�h���!��z�&��a�ݟ�1�㌟�ܡ��
��R*�Ht��C^˥V�N	d���ڜF�J�4�˲ ?j��5�5QMډ��6��`>�h����ٚM��DFb�Ts���>e�ҁՍ���w���6�¹Uف����A�J�LZ�O+�οBp߰D�YC;6�:��j%6�6w`����8?_f�w      @   �   x�U̱
�0����)��H�M�f��`q�[����(�o_�R�t����%�X�������+ni~��i9u8[{�FM53�~��x�V�HR�	�MX#��Ot����fu�O����tyK?��+fe0��XKb���B�#�2�     